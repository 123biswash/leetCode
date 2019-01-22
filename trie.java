public class Trie{

    private class TrieNode {
        Map <Character, TrieNode> children;
        boolean endOfWord;
        public TrieNode(){
            children=new HashMap<>();
            endOfWord=false;
        }
    }

    private final TrieNode root;
    public Trie(){
        root = new TrieNode();
    }
    //insert 
    public void insert(String word){
        TrieNode current = root;
        for(int i =0;i<word.length();i++){
            char ch = current.children.get(ch);
            if (node==null){
                node=new TrieNode();
                current.children.put(ch, node);
            }
            current = node;
        }
        //mark current words' endOfWord as true
        current.endOfWord=true;
    }
}