import java.io.*;
import java.util.*;

class Node {
    public Node parent;
    public LinkedList<Node> connections = new LinkedList<>();
    public int value;
    Node (int value) {
        this.value = value;
    }

    void addConnection(Node dest) {
        connections.add(dest);
    }

    void setChildrensParent() {
        if (this.parent == null) return;
        else {
            for (int i = 0; i < connections.size(); i++) {
                Node dst = connections.get(i);
                if (dst == parent) continue;
                dst.parent = this;
                dst.setChildrensParent();
            }
        }
    }
}

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());
        Node[] nodes = new Node[N + 1];
        for (int i = 0; i < N + 1; i++) nodes[i] = new Node(i);
        nodes[1].parent = nodes[0];
        nodes[1].setChildrensParent();
        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int src = Integer.parseInt(st.nextToken());
            int dst = Integer.parseInt(st.nextToken());
            nodes[src].addConnection(nodes[dst]);
            nodes[dst].addConnection(nodes[src]);
        }
        nodes[1].setChildrensParent();
        for (int i = 2; i < N + 1; i++) System.out.println(nodes[i].parent.value);        
    }
}