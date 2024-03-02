def activitySelection(start, end):
    selectedTask = [0]

    j = 0
    for i in range(1,len(start)):
        if end[j] <= start[i]:
            selectedTask.append(i)
            j = i
    return selectedTask



start = [ 10, 12, 20,35,39]
end = [20, 25, 30,40,40]

print(activitySelection(start,end))