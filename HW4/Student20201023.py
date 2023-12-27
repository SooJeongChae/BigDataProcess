#!/usr/bin/python3

import numpy as np
import operator

def createDataSet(text, i):
    group = np.array(text) # 배열 생성
    labels = [i] # 각 데이터와 매칭되는 라벨 리스트
    return group, labels

def classify0(inX, dataSet, labels, k):
     # 거리 계산 (Euclidian distance)
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) – dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1) # 주어진 axis로 배열 요소들의 합계 반환
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort() # 배열 소팅 후 인덱스 반환
    classCount = {}
    for i in range(k): # 가장 짧은 거리를 투표
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), # 아이템 정렬
        key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList): # 모든 분류 항목이 같으면
        return classList[0] # 멈추고 그 분류 항목 표시를 반환
    if len(dataSet[0]) == 1: # 분류할 속성이 더 이상 없으면
        return majorityCnt(classList) # 가장 많은 수를 반환함
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}} # 유일한 값의 리스트를 구함
    del(label[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = # 데이터 집합을 분할할 때마다 recursive call
            createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


study, test = input('').split()

for i in 10:
    for j in 10:
        try:
            f = open(study\i_j.txt, "rt")
            text = f.read()
            list_text = list(text)
            group, labels = createDataSet(list_text, i)
        except FileNotFoundError:
            print("파일이 없습니다. ")
        finally:
            f.close()

for i in 10:
    for j in 10:
        try:
            f = open(test\i_j.txt, "rt")
            te = f.read()
            list_te = list(te)
            classify0(list_te, group, labels, 9)
        except FileNotFoundError:
            print("파일이 없습니다. ")
        finally:
            f.close()
