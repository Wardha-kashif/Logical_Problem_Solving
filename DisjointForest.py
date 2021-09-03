# #Disjoint Forest is basically used for Mutual Friendship Problems
#
# #It is a disjoint set. If two elements are in the same tree, then they are in the same disjoint set
#
#
# # / Finds the representative of the set
# # // that i is an element of
# # int find(int i)
# # {
# #     // If i is the parent of itself
# #     if (parent[i] == i)
# #     {
# #         // Then i is the representative of
# #         // this set
# #         return i;
# #     }
# #     else
# #     {
# #         // Else if i is not the parent of
# #         // itself, then i is not the
# #         // representative of his set. So we
# #         // recursively call Find on its parent
# #         return find(parent[i]);
# #     }
# # }
#
# # // Unites
# # the
# # set
# # that
# # includes
# # i
# # // and the
# # set
# # that
# # includes
# # j
# # void
# # union(int
# # i, int
# # j)
# # {
# # // Find
# # the
# # representatives
# # // (or the root nodes)
# # for the set
# #         // that includes i
# #
# # int irep = this.Find(i),
# #
# # // And do the same for the set
# # // that includes j
# # int jrep = this.Find(j);
# #
# # // Make the parent of i’s representative
# # // be j’s  representative effectively
# # // moving all of i’s set into j’s set)
# # this.Parent[irep] = jrep;
# # }
#
#
#
# // Unites the set that includes i and the set
# // that includes j
# void union(int i, int j)
# {
#     // Find the representatives (or the root nodes)
#     // for the set that includes i
#     int irep = this.find(i);
#
#     // And do the same for the set that includes j
#     int jrep = this.Find(j);
#
#     // Elements are in same set, no need to
#     // unite anything.
#     if (irep == jrep)
#         return;
#
#     // Get the rank of i’s tree
#     irank = Rank[irep],
#
#     // Get the rank of j’s tree
#     jrank = Rank[jrep];
#
#     // If i’s rank is less than j’s rank
#     if (irank < jrank)
#     {
#         // Then move i under j
#         this.parent[irep] = jrep;
#     }
#
#     // Else if j’s rank is less than i’s rank
#     else if (jrank < irank)
#     {
#         // Then move j under i
#         this.Parent[jrep] = irep;
#     }
#
#     // Else if their ranks are the same
#     else
#     {
#
#         // Then move i under j (doesn’t matter
#         // which one goes where)
#         this.Parent[irep] = jrep;
#
#         // And increment the result tree’s
#         // rank by 1
#         Rank[jrep]++;
#     }
# }


# Python3 program to implement Disjoint Set Data
# Structure.

class DisjSet:
    def __init__(self, n):
        # Constructor to create and
        # initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    # Finds set of given item x
    def find(self, x):

        # Finds the representative of the set
        # that x is an element of
        if (self.parent[x] != x):
            # if x is not the parent of itself
            # Then x is not the representative of
            # its set,
            self.parent[x] = self.find(self.parent[x])

        # so we recursively call Find on its parent
        # and move i's node directly under the
        # representative of this set

        return self.parent[x]

    # Do union of two sets represented
    # by x and y.
    def Union(self, x, y):

        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)

        # If they are already in same set
        if xset == yset:
            return

        # Put smaller ranked item under
        # bigger ranked item if ranks are
        # different
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        # If ranks are same, then move y under
        # x (doesn't matter which one goes where)
        # and increment rank of x's tree
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1


# Driver code
obj = DisjSet(5)
obj.Union(0, 2)
obj.Union(4, 2)
obj.Union(3, 1)
if obj.find(4) == obj.find(0):
    print('Yes')
else:
    print('No')
if obj.find(1) == obj.find(0):
    print('Yes')
else:
    print('No')



