# avl
AVL Binary search trees (without duplicates) + Unordered lists with log time insertion/removal, implementation in Python 3.

API:
+ __Node__ class:
    - __elt__: stored data
    - __n__: tuple of left/right nodes
    - __h__: tuple of left/right heights
    - __s__: tuple of left/right subtree sizes
    - __fix(node,b)__: sets the left or right node of the original node, and rebalances the tree
    - __traverse(check,ret,use,x)__: inorder traversal of the subtree of given node (with x set to the index of the node)
        * __check(node,x)__: boolean function that terminates traversal when True
        * __ret(node,x)__: function called on each traversed node, returning desired information
        * __use(al,a,ar)__: function that combines information from node and both subtrees, and passes upwards
      Note that the default value of al and ar are always (None,0).
      
      As an example, the following call returns the maximum of a non-empty unordered list u:
      
          check = lambda n, x: 0
          ret = lambda n, x: n.elt
          z = lambda a, b: max(a, b) if b else a
          use = lambda al, a, ar: z(z(a, al[0]), ar[0])
          return u.h.traverse(check, ret, use, u.h.s[0])[0]
          
+ __AVL__ class:
    - __find(elt)__: binary searches the position where elt should be inserted in the tree
    - __get(i)__: get the value stored at index i
    - __add(elt)__: add elt to the tree
    - __delt(elt)__: remove elt from the tree if present
    - __dpos(i)__: remove elt stored at index i
    - __disp()__: returns string containing the contents of the tree

+ __Ulist__ class (inherited from AVL):
    - __add(elt,i)__: inserts elt before index i (or appends to end if i is unassigned)
    - __find(elt)__: returns the first index of an element equal to elt, or -1 if none exist
