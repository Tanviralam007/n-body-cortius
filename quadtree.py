'''
contain 2 classes:
    Quadtree
    Boundary
'''

class Boundary:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contains(self, particle):
        return (
            self.x - self.width <= particle.x <= self.x + self.width and
            self.y - self.height <= particle.y <= self.y + self.height
        )

class Quadtree:
    CAPACITY = 1
    def __init__(self, boundary):
        self.boundary = boundary
        self.particles = []
        self.divided = False
        self.northwest = self.northeast = self.southwest = self.southeast = None

    def subdivide(self):
        x, y = self.boundary.x, self.boundary.y
        w, h = self.boundary.width / 2, self.boundary.height / 2

        self.northwest = Quadtree(Boundary(x - w, y - h, w, h))
        self.northeast = Quadtree(Boundary(x + w, y - h, w, h))
        self.southwest = Quadtree(Boundary(x - w, y + h, w, h))
        self.southeast = Quadtree(Boundary(x + w, y + h, w, h))
        self.divided = True

    def insert(self, particle):
        if not self.boundary.contains(particle):
            return False
        
        if len(self.particles) < self.CAPACITY:
            self.particles.append(particle)
            return True
        else:
            if not self.divided:
                self.subdivide()
            if self.northwest.insert(particle): return True
            if self.northeast.insert(particle): return True
            if self.southwest.insert(particle): return True
            if self.southeast.insert(particle): return True
        return False

