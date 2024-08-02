class Node:
    def __init__(self, name, is_file = False):
        self.name = name
        self.children_map = {}
        self.is_file = is_file
        self.file_content = ''

class FileSystem:
    def __init__(self):
        self.root_node = Node('')

    def ls(self, path: str) -> List[str]:
        fileNode = self._traverse(path)
        if fileNode.is_file:
            return [fileNode.name]
        else:
            return sorted(fileNode.children_map.keys())

    def mkdir(self, path: str) -> None:
        self._traverse(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        fileNode = self._traverse(filePath)
        fileNode.is_file = True
        fileNode.file_content += content

    def readContentFromFile(self, filePath: str) -> str:
        fileNode = self._traverse(filePath)

        return fileNode.file_content
    
    # fetch node of the filePath. If doesn't exist, create path
    def _traverse(self, filePath: str) -> Node:
        if filePath == '/': # root
            return self.root_node
        
        path = filePath.split('/')
        node = self.root_node
        for p in path[1:]:
            if p not in node.children_map:
                node.children_map[p] = Node(p)
            node = node.children_map[p]
        return node

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
