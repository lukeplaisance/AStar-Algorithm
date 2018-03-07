#pylint: disable = E1101
#pylint: disable = C0330
from draw_shapes import Rectangle
from vector2 import Vector2

class VisualNode(object):
    '''class to see the node on the grid'''
    def __init__(self, node, surface, pos, scale):
        self.node = node
        self.shape = Rectangle(surface, (200, 200, 200), pos, scale)

    def draw(self):
        '''function to draw the node'''
        self.shape.draw_rect()

class VisualGraph(object):
    '''class to see the grid in the window'''
    def __init__(self, graph, offset, surface):
        self.graph = graph
        self.offset = offset
        self.surface = surface
        self.node_visual = []

    def gen_visual(self):
        '''function to generate the visual graph'''
        count = 0
        for x in range(0, self.graph.width * self.offset, self.offset):
            for y in range(0, self.graph.height * self.offset, self.offset):
                new_node = VisualNode(self.graph.nodes[count], self.surface,
                                        Vector2(x, y), [25, 25])
                self.node_visual.append(new_node)
                count += 1

