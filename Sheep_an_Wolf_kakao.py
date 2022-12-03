class NODE:
    Max = 0
    info = []
    edge = []
    def __init__(self,num,sheep,wolf,nodes):
        self.num = num           #현재 위치 노드
        self.sheep = sheep
        self.wolf = wolf
        self.nodes = nodes       #이동 가능 노드
        /87
    def check(self):/
        if self.sheep > self.wolf:
            return True
        return False
    
    def add(self,cur):
        self.sheep += cur ^ 1
        self.wolf += cur
        
    def Maxcheck(self):
        NODE.Max = self.sheep if self.sheep > NODE.Max else NODE.Max
        
def solution(info, edges):
    edge = [[] for i in range(len(info))]
    
    for i in edges:
        edge[i[0]].append(i[1])     #간선 입력
        
    NODE.edge = edge
    NODE.info = info      #클래스 변수에 노드 정보 입력
    
    DFS(NODE(0,0,0,edge[0]))
    answer = NODE.Max
    return answer

def DFS(Node):
    cur = NODE.info[Node.num]
    Node.add(cur)              #현재 노드에 잇는 동물 추가
    
    if Node.check():           #양이 더 많을 시 순회
        for i in Node.nodes:   #이동 가능 노드 전체를 순회
            nodes = Node.nodes.copy()
            nodes.remove(i)          #목표 노드를 이동 가능 노드에서 제외
            for n in NODE.edge[i]:   #목표 노드에서 이동 가능한 노드 추가
                nodes.append(n)
            DFS(NODE(i,Node.sheep,Node.wolf,nodes))    #이동 가능한 노드들을 기억 후 순회
    else:
        pass
    Node.Maxcheck()             #가능한 최대 양 수 기록
