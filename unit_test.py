from vector2 import Vector2
from GraphClass import Graph
from A_starClass import Astar
import random

#DO NOT MODIFY
class Node(object):
    '''Class that will be used to create node objects. These objects
    will be used in the path finding algorithm known as A_Star'''
    def __init__(self, pos):
        self.position = pos
        self.parent = None
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.traversable = True
        self.is_goal = False
        self.is_start = False

    def change_state(self, state):
        '''Changes the value of the state specified with the value of state
        passed in. If the state was currently true on funciton call it will
        be set to false'''
        if state == "start":
            self.is_start = not self.is_start
        if state == "goal":
            self.is_goal = not self.is_goal
        if state == "wall":
            self.traversable = not self.traversable

    def set_parent(self, node):
        '''Attempts to change the value of the parent variable. If the value is
        None the parent is automaticly set to the value of node passed in. Otherwise
        a new G score is calcualted and if it is cheaper than the current the parent
        is changed to the node passed in and the G score is modified to reflect the
        change in parents'''
        if self.parent is None:
            self.parent = node
            return True
        else:
            temp_g = node.g_score
            if self.position.x_pos is node.position.x_pos or self.position.y_pos is node.position.y_pos:
                temp_g += 10
            else:
                temp_g += 14
            if temp_g < self.g_score:
                self.parent = node
                self.g_score = temp_g
            return False

    def calculate_g_score(self, node):
        '''Calculates the movement cost to move from nodes parent to it self. If the
        movement is horizontal or vertical the cost is parent's G score + 10. If the
        movement is diagonal the cost is parent's G score + 14'''
        if self.set_parent(node) is True:
            self.g_score = node.g_score
            if self.position.x_pos is node.position.x_pos or self.position.y_pos is node.position.y_pos:
                self.g_score += 10
            else:
                self.g_score += 14

    def calculate_h_score(self, goal):
        '''Calculates the estimated movement cost to move from this node to the goal.'''
        self.h_score = 10 * (abs(goal.position.x_pos - self.position.x_pos) +
                             abs(goal.position.y_pos - self.position.y_pos))

    def calculate_f_score(self):
        '''Calculates the fscore which is the sum of the H score and G score of the node'''
        self.f_score = self.g_score + self.h_score

    def __str__(self):
        return str.format("<{0},{1}>", self.position.x_pos, self.position.y_pos)

def get_neighbors(node, graph):
    '''Gets the neighbors of the node. Used to generate the correct path for the user to
    test against'''
    right = Vector2(node.position.x_pos + 1, node.position.y_pos)
    top_right = Vector2(node.position.x_pos + 1, node.position.y_pos + 1)
    top = Vector2(node.position.x_pos, node.position.y_pos + 1)
    top_left = Vector2(node.position.x_pos - 1, node.position.y_pos + 1)
    left = Vector2(node.position.x_pos - 1, node.position.y_pos)
    bottom_left = Vector2(node.position.x_pos - 1, node.position.y_pos - 1)
    bottom = Vector2(node.position.x_pos, node.position.y_pos - 1)
    bottom_right = Vector2(node.position.x_pos + 1, node.position.y_pos - 1)
    directions = [right, top_right, top, top_left,
                  left, bottom_left, bottom, bottom_right]
    neighbors = []
    for node in graph:
        for position in directions:
            if node.position == position:
                neighbors.append(node)
    return neighbors

def correct_test(start, goal, graph):
    '''Geneartes the correct path that the users algorithm will be tested against'''
    open_list = []
    closed_list = []
    current_node = start
    open_list.append(current_node)
    while goal not in closed_list or open_list.count == 0:
        open_list.sort(key=lambda node: node.f_score)
        current_node = open_list[0]
        open_list.remove(current_node)
        closed_list.append(current_node)
        if closed_list.__contains__(goal):
            break
        neighbors = get_neighbors(current_node, graph)
        for node in neighbors:
            if not node.traversable or node in closed_list:
                continue
            node.calculate_g_score(current_node)
            node.calculate_h_score(goal)
            node.calculate_f_score()
            if open_list.__contains__(node):
                continue
            open_list.append(node)
        if len(open_list) == 0:
            return []
    path = []
    if closed_list.__contains__(goal):
        path_node = goal
        while path_node is not None:
            path.append(path_node)
            path_node = path_node.parent
    return path
 
def shuffle_search_space():
    '''Generates the search space to test the algorithm in'''
    graph = []
    for x_pos in range(10):
        for y_pos in range(10):
            graph.append(Node(Vector2(x_pos, y_pos)))
    rand_start_index = random.randrange(0, 99)
    rand_goal_index = random.randrange(0, 99)
    num_walls = random.randrange(0, 25)
    start_node = graph[rand_start_index]
    goal_node = graph[rand_goal_index]
    blockers = []
    for counter in range(num_walls):
        blocker = graph[random.randrange(0, 99)]
        blocker.traversable = False
        blockers.append(blocker)
    return [graph, start_node, goal_node, blockers]

def test_function(func):
    '''Pass in the function you wish to test. Function must take in three arguments.
    First argument is the start node.
    Second Argument is the goal node.
    Thrid Argument is the search space'''
    test_case = shuffle_search_space()
    graph = test_case[0]
    start_node = test_case[1]
    goal_node = test_case[2]
    blockers = test_case[3]
    result = func(start_node, goal_node, graph)
    correct = correct_test(start_node, goal_node, graph)
    str_blockers = ""
    str_correct = ""
    str_result = ""
    for node in blockers:
        str_blockers = str_blockers + str(node)
    for node in result:
        str_result = str_result + str(node)
    for node in correct:
        str_correct = str_correct + str(node)
    line = str.format("start::{0} goal::{1} walls::{2}\n", str(start_node),
                      str(goal_node), str_blockers)
    line2 = str.format("Expected Result:: {0}\nActual Result:: {1}", str_correct, str_result)
    print line, line2
    if len(result) != len(correct):
        print "Fail Test"
        return 0
    for i in range(len(result)):
        if result[i].position != correct[i].position:
            print "Fail Test"
            return 0
    print "Pass Test"
    return 1
#DO NOT MODIFY

def main():
    '''the main'''
    grid = Graph(10, 10)
    start = grid.nodes[53]
    end = grid.nodes[57]
    num_test = 10
    num_passed = 0
    test1 = Astar(start, end, grid)
    verdict = test_function(test1.path)
    num_passed = num_passed + verdict
    print str.format("Number of Test::{0} Number Passed::{1}", num_test, num_passed)

main()
