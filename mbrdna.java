import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/** 
 * Your first line of input will be a comma separated pre-order traversal of a binary tree.
 * Your second line of input will be a comma separated in-order traversal of the same binary tree.
 * 
 * Output the post-order traversal of the binary tree on a single line.
 */
public class Solution {
    public static void main(String args[] ) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        
        /* EXAMPLE USAGE OF NODE
        Solution.Node node = new Solution.Node(1, null, null);
        System.out.println(node.value);
        */
        Scanner scanner = new Scanner(System. in);
        String[] preOrderStrings = scanner.nextLine().split(",");
        String[] inOrderStrings = scanner.nextLine().split(",");
        int getRoot = findRoot(preOrderStrings, inOrderStrings);
        printPostTraversal(getRoot);
    }
    
    /**
     * PROVIDED
     */
    static class Node {
        public int value;
        public Solution.Node left;
        public Solution.Node right;
        
        public Node (int v, Solution.Node left, Solution.Node right) {
            this.value = v;
            this.left = left;
            this.right = right;
        }
    }
    public static Solution.Node findRoot(List<Integer> pre, List<Integer> inOrder){
        int preRoot = pre.get(0);
        int foundValue=0;
        int foundIndex=0;
        
        int listSize = inOder.size();
        List<Integer> inLeft= new List<Integer>(listSize);
        List<Integer> inRight= new List<Integer>(listSize);
        List<Integer> preLeft= new List<Integer>(listSize);
        List<Integer> preRight= new List<Integer>(listSize);
        for (int i=0;i<inOrder.size();i++){
            if (inOrder[i]==preRoot){
                foundValue=inOrder[i];
                foundIndex=i;
            }
        }
        inLeft=inOder.sublist(0,foundIndex);
        inRight=inOder.sublist(foundIndex+1,listSize);
        //same with Pre
        Solution.Node returnRoot = new Solution.Node(foundValue, NULL, NULL);
        returnRoot.left = //RECURSE 
        return returnRoot;
    }
    public static void printPostTraversal(Solution.Node rootNode){
        if (rootNode==null){
            return;
        }
        printPostTraversal(rootNode.left);
        printPostTraversal(rootNode.right);
        System.out.print(rootNode.value);
        return;
    }
    
    /*
    
inOrder
foundValue=5
foundIndex=4

inOder[0:foundIndex-1]->leftSub
inOder[foundIndex+1:inOrder.length()-1]->right

L => pre, inOrder
R =>
N 
    */
}