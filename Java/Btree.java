public class Btree {
    
    public Node root;

    Btree() {
        // new root
        root = new Node();
        // assign the root node to be a isLeaf
        root.isLeaf = true;
        root.numberOfNodes = 0;
        // initial the key value in the root to -1 (null)
        root.key[0] = -1;
    }

   
    public void insert(int k)
    {
        
        Node r = root;
       
        if (r.numberOfNodes == 3) {
            // Create a new node s
            Node s = new Node();
            // the new node s will become a new root node after root node r gets spilt
            root = s;
            s.numberOfNodes = 0;
            // the new root node is no longer a isLeaf
            s.isLeaf = false;
            s.children[0] = r;

            //Call the split method to split the node r because it is full
            splitChild(s, 1, r);
            //Call the insert in none full node method to insert the key k into the new node s
            insertNonfull(s, k);
        } // If the root r node is not full, just insert the key k into it by calling the insert in none full node method
        else {
            insertNonfull(r, k);
        }
    }

   
    public void insertNonfull(Node node, int value) {
        // Alocate the node 
        int i = node.numberOfNodes;
        // if the node is a isLeaf, we insert the value into the node 
        if (node.isLeaf) {
            while (i >= 1 && value < node.key[i - 1]) {
                node.key[i] = node.key[i - 1];
                i--;
            }
            node.key[i] = value;
            node.numberOfNodes++;
        } 
         else {
            while (i >= 1 && value < node.key[i - 1]) {
                i--;
            }
            i++;
            // if the node is full, split it.
            if (node.children[i - 1].numberOfNodes == 3) {
                // call the Split child method to split the node to two nodes
                splitChild(node, i, node.children[i - 1]);
                // Determine which of the two children is now the correct one to descend to.
                if (value > node.key[i - 1]) {
                    i++;
                }
            }
            // Recursive Call
            insertNonfull(node.children[i - 1], value);
        }
    }

    public void splitChild(Node parentNode, int childIndex, Node newChild) {
        // Create a new node z, z will be the new child of node x
        Node z = new Node();
        z.isLeaf = newChild.isLeaf;
        z.numberOfNodes = 1;   // fix it to t-1
        z.key[0] = newChild.key[2];

        // if node y is not a isLeaf, assign the largest t-1 keys and child to the node z.
        if (!newChild.isLeaf) {
            z.children[1] = newChild.children[3];
            z.children[0] = newChild.children[2];
        }
        newChild.numberOfNodes = 1; // fix it to t -1

        // Here we insert node z as a child of node x
        for (int j = parentNode.numberOfNodes + 1; j >= childIndex + 1; j--) {
            parentNode.children[j] = parentNode.children[j - 1];
            parentNode.key[j - 1] = parentNode.key[j - 2];
        }
        // assign the reference to the node z ( node z is a child of the node x)
        parentNode.children[childIndex] = z;
        parentNode.key[childIndex - 1] = newChild.key[1];
        // increment
        parentNode.numberOfNodes++;
    }

    
    public boolean search(Node node, int value) {
        // initial i to be equal to 1
        int i = 1;
        
        while (i <= node.numberOfNodes && value > node.key[i - 1]) {
            //increment i
            i++;
        }
        if (i <= node.numberOfNodes && value == node.key[i - 1]) {
            // return true if the key k is found in the B Tree
            return true;
        }
        
        if (!node.isLeaf) {
            // recursive call to search in the subtree of the node x
            return search(node.children[i - 1], value);
        }
        return false;
    }

  
    public boolean search(int k) {
        // assign the node x to be the root and start search from the root
        Node x = root;
        // send the root x and the key k as an arguments to the the method search above
        return search(x, k);
    }

    public boolean delete(int k) {
        Node x = root; // getting the root node
        return delete(x, k); // calling the delete with the root node as starting point
    }

    
    public boolean delete(Node node, int value) {
        // look up for a key k that will be deleted
        int i = 1;
//---
        // find the smallest index i such that k<= x.keyi, or else set i to x.n ++
        while (i <= node.numberOfNodes && value > node.key[i - 1]) {
            //increment i
            i++;
        }
        /* if the x node is an internal node, terminate the search unsuccessful or 
         * recurse to search the appropriate subtree of node x.
         */
        // if the node is a is Leaf
        if (node.isLeaf) {
            // recursive call to search in the subtree of the node x
            // check if the key k is found
            if (i <= node.numberOfNodes && value == node.key[i - 1]) {
                // return true if the key k is found in the B Tree
                node.key[i - 1] = 0;
                // Deleting and sifting
                for(int j = i - 1; j < node.numberOfNodes - 1; j++){
                    node.key[j] = node.key[j+1];
                    if(j+1 == node.numberOfNodes - 1)
                        node.numberOfNodes--;                    
                }
                return true;
            }
        } else {
            return delete(node.children[i - 1], value);
        }
        // return false if the key k is not found in the B Tree
        return false;
    }
    
    /**
     * To print the B-Tree
     */
    public void print() {
        // Call the printBtree Method to print the B-Tree
        printBtree(root, "");
    }
    
    /**
     * This Method is to print the B-Tree
     * @param node the node to be printed
     * @param indent the wanted indent.
     */
    public void printBtree(Node node, String indent) {
        // if the node is null print "The B-Tree is Empty"
        if (node == null) {
            System.out.println(indent + "The B-Tree is Empty");
        } else {
            System.out.println(indent + " ");

            // declare a string variable
            String childIndent = indent + "\t";

            // for loop to print the B-Tree, recursively print the B-Tree Strucure
            for (int i = node.numberOfNodes-1; i >= 0; i--) {
                if (!node.isLeaf) // Recursive Call
                {
                    printBtree(node.children[i], childIndent);
                }
                // print the keys
                if(node.key[i] > 0)
                    System.out.println(childIndent + node.key[i]);
            }
            if (!node.isLeaf) // Recirsive Call
            {
                printBtree(node.children[node.numberOfNodes], childIndent);
            }
        }
    }
}