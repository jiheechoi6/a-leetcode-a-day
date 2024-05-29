class FileSystem {
    private static class Node {
        private final String name;
        private final Map<String, Node> nodeByName = new TreeMap<>(); // if node is directory
        private final StringBuilder content = new StringBuilder(); // if node if file
        private boolean isFile;

        Node(final String name){
            this.name = name;
        }
    }

    private final Node root = new Node("");

    public FileSystem() {}
    
    public List<String> ls(String path) {
        Node node = traversePath(path);
        return node.isFile ? List.of(node.name) : List.copyOf(node.nodeByName.keySet());
    }
    
    public void mkdir(String path) {
        traversePath(path);
    }
    
    public void addContentToFile(String filePath, String content) {
        Node file = traversePath(filePath);
        file.isFile = true;
        file.content.append(content);
    }
    
    public String readContentFromFile(String filePath) {
        return traversePath(filePath).content.toString();
    }

    private Node traversePath(String path){
        Node current = root;
        String[] pathLst = path.split("/");
        
        for(int i = 1; i<pathLst.length; i++){
            final int ic = i;
            current = current.nodeByName.computeIfAbsent(pathLst[i], k -> new Node(pathLst[ic]));
        }
        return current;
    }
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem obj = new FileSystem();
 * List<String> param_1 = obj.ls(path);
 * obj.mkdir(path);
 * obj.addContentToFile(filePath,content);
 * String param_4 = obj.readContentFromFile(filePath);
 */
