#!/usr/bin/env python3
from typing import Type

import numpy as np
import pymongo as mongo

import Shogi_Game as game
from Shogi_Game import board



def set_Up_Knn_move(piece_move_set):
    import numpy as np
    from sklearn.tree import DecisionTreeClassifier

    import pymongo as mongo
    client = mongo.MongoClient("mongodb+srv://ShogiServer:3VNBodyaiUL6HtE0@cluster0-pfhah.mongodb.net/test")
    mydb = client["Shogi"]
    collection = mydb["gameHistory"]

    dataset = []

    for x in collection.find({}, {"_id": 0}):
        temp = []
        for x in x["moves"]:

            if x[121] in piece_move_set:
                dataset.append(x)

    dataset = np.array(dataset)
    fields = dataset[:, :-3]
    targets = dataset[:, -3:]

    knn = DecisionTreeClassifier()
    return knn.fit(fields, targets)

def set_Up_Knn(piece_nums):
    print('setting up nn')
    import numpy as np
    from sklearn.tree import DecisionTreeClassifier

    import pymongo as mongo
    client = mongo.MongoClient("mongodb+srv://ShogiServer:3VNBodyaiUL6HtE0@cluster0-pfhah.mongodb.net/test")
    mydb = client["Shogi"]
    collection = mydb["gameHistory"]

    dataset = []

    for x in collection.find({}, {"_id": 0}):
        temp = []
        for x in x["moves"]:

            if x[120] in piece_nums:
                dataset.append(x)

    dataset = np.array(dataset)
    fields = dataset[:, :-3]
    targets = dataset[:, -3:]

    knn = DecisionTreeClassifier()
    return knn.fit(fields, targets)


def convertTakenBoard(x, y):
    val = 0;
    if (y == 1):
        if (x == 11):
            val = 200

        if (x == 12):
            val = 201

        if (x == 13):
            val = 202

        if (x == 14):
            val = 203

    elif (y == 2):
        if (x == 11):
            val = 220

        if (x == 12):
            val = 221

        if (x == 13):
            val = 222

        if (x == 14):
            val = 223
    return val


def convertBackToStandardTakenBoard(num):
    x = 0
    y = 1
    if (num > 210):
        y = 2
    switcher = {
        200: 11,
        201: 12,
        202: 13,
        203: 14,
        220: 11,
        221: 12,
        222: 13,
        223: 14
    }
    return switcher.get(num), y
def checkForAutoResign():
    import pymongo as mongo


    import datetime

    xt = datetime.date.today()
    x = xt.replace(month=datetime.date.today().month-1)

    client = mongo.MongoClient("mongodb+srv://ShogiServer:3VNBodyaiUL6HtE0@cluster0-pfhah.mongodb.net/test")
    mydb = client["Shogi"]
    collectionGame = mydb["games"]

    que = {"lastPlayDate": "x", }
    try:
        for x in collectionGame.find(que):
            print(x)
            playerTurn = x["playerTurn"]
            if playerTurn == x["userOne"]:
                winner = x["userTwo"]
            else:
                winner = x["userOne"]
            setter = {"$set": {"gameEnd": xt,"winner": winner}}

            collectionGames.update_one(x, setter)
    except Exception as e:
        print(e)

# main program
import dns


client = mongo.MongoClient("mongodb+srv://ShogiServer:3VNBodyaiUL6HtE0@cluster0-pfhah.mongodb.net/test")

mydb = client["Shogi"]

import time

t = True
start = time.time()


while (True):

    end = time.time()
    #if (end - start) > 86400.0:
        #checkForAutoResign()
    collectionGames = mydb["games"]

    testData = []
    gameId = []
    query = {"playerTurn": "CPU", }

    playerPieces = []
    playerPiecesX = []
    playerPiecesY = []
    oppPieces = []
    oppPiecesX = []
    oppPiecesY = []
    promoted = []
    array = []
    try:
        for x in collectionGames.find(query).limit(1):

            gameId.append(x["gameId"])
            promoted = x["promoted"]
            playerPieces = x["moves"]["movesPlayer"]["pieces"]

            playerPiecesX = x["moves"]["movesPlayer"]["Xcoords"]
            playerPiecesY = x["moves"]["movesPlayer"]["Ycoords"]
            oppPieces = x["moves"]["movesOpp"]["pieces"]
            oppPiecesX = x["moves"]["movesOpp"]["Xcoords"]
            oppPiecesY = x["moves"]["movesOpp"]["Ycoords"]
            pxIter = iter(playerPiecesX)
            pyIter = iter(playerPiecesY)
            oxIter = iter(oppPiecesX)
            oyIter = iter(oppPiecesY)



            for x in range(1, 41):
                if (x in promoted):
                    array.append(x)
                if (x not in promoted):
                    array.append(0)

            mapOfPlayer = dict()
            for x in iter(playerPieces):
                xCoord = next(pxIter)

                mapOfPlayer[x] = xCoord + (next(pyIter) - 1) * 9

            mapOfOpp = dict()
            for x in iter(oppPieces):
                xCoord = next(oxIter)

                mapOfOpp[x] = xCoord + (next(oyIter) - 1) * 9


            for x in range(1, 41):
                if (x in mapOfPlayer):
                    array.append(mapOfPlayer.get(x))
                if (x not in mapOfPlayer):
                    array.append(0)

            for x in range(1, 41):
                if (x in mapOfOpp):
                    array.append(mapOfOpp.get(x))
                if (x not in mapOfOpp):
                    array.append(0)

        brd = board(playerPieces, playerPiecesX, playerPiecesY, oppPieces, oppPiecesX, oppPiecesY,
                    promoted)
        print(brd.get_player_two_pieces_nums())
        knn = set_Up_Knn(brd.get_player_two_pieces_nums())

        testData = np.array(array)
        print(gameId[0])
        print(testData.reshape(1, -1).shape)

        # predicted move
        result = knn.predict(testData.reshape(1, -1))
        print('piece ' + str(int(result[0][0])))
        print('move ' + str( int(result[0][1])))




        # check if a valid move
        print("pulling initial x and y")

        xy = brd.get_player_piece_location_on_board(result[0][0])
        print(brd.get_player_piece_at_location(xy[0],xy[1]).piece_type)
        piece_to_move = brd.get_player_piece_at_location(xy[0], xy[1])
       # print(game.get_list_of_move_set_as_positions( piece_to_move.move_set()))


        movXY = brd.find_best_move( xy[0], xy[1],int(result[0][1]))

        print("pulling post x and y")

        print("moving on board" + str(movXY) + str(xy))
        moved = brd.move_piece_on_board(int(xy[0]), int(xy[1]), int(movXY[0]), int(movXY[1]))

        if(moved):
            print(brd.get_player_piece_location_on_board(result[0][0]))


        # update database
            print("unpacking board")
            player_piece_nums, player_piece_x, player_piece_y, opp_piece_nums, opp_piece_x, opp_piece_y, promotelist = brd.get_board_as_arrays()
            query = {"gameId": gameId[0]}
            values = {"$set": {"moves": {
                "movesPlayer": {"pieces": player_piece_nums, "Xcoords": player_piece_x, "Ycoords": player_piece_y}
                , "movesOpp": {"pieces": opp_piece_nums, "Xcoords": opp_piece_x, "Ycoords": opp_piece_y}}
            }
             }

            collectionGames.update_one(query, values)

        # set promote list

        # change turn
            query = {"gameId": gameId[0]}
            for x in collectionGames.find(query).limit(1):
                print(x["userOne"])

            setter = {"$set": {"playerTurn": x["userOne"]}}

            collectionGames.update_one(query, setter)

        # change turn number
            query = {"gameId": gameId[0]}
            for x in collectionGames.find(query).limit(1):
                print(x["turnNumber"])

            setter = {"$set": {"turnNumber": x["turnNumber"] + 1}}

            collectionGames.update_one(query, setter)


    except Exception as e:
        print(e)
        print("no computer turns")

        time.sleep(13)

    # check for games that have not had a move for 30 days and force resign

