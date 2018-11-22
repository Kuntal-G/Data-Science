# Tower of Hanoi Problem


def towerHanoi(height,fromRod,toRod,auxRod):

    if height==1:
        print('Moved disk 1 from {} to {}'.format(fromRod, toRod))

    else:
        towerHanoi(height-1,fromRod,auxRod,toRod)
        print('Moved disk {} from {} to {}'.format(height,fromRod,toRod))
        towerHanoi(height-1,auxRod, toRod,fromRod)


n = 4
towerHanoi(n, 'A', 'C', 'B')