import java.util.Scanner;
import java.util.Stack;
//재귀 버전 dfs
public class Main {
    static boolean[] visited = new boolean[9];
    static int[][] graph = {{}, {2,3,8}, {1,6,8}, {1,5}, {5,7}, {3,4,7}, {2}, {4,5}, {1,2}};
    static void dfs(int nodeIndex){
        visited[nodeIndex]=true;
        System.out.print(nodeIndex+" -> ");
        for(int node : graph[nodeIndex]){
            if(!visited[node]){
                dfs(node);
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        dfs(1);
        sc.close();
    }
}

//스택 버전 dfs
public class Main{
    static boolean[] visited= new boolean[9];
    static int[][] graph = {{}, {2,3,8}, {1,6,8}, {1,5}, {5,7}, {3,4,7}, {2}, {4,5}, {1,2}};
    static Stack<Integer> stack = new Stack<>();
    public static void main(String[] args){
        stack.push(1);
        visited[1]=true;
        while(!stack.isEmpty()){
            int nodeIndex = stack.pop();
            System.out.println(nodeIndex);
            for (int LinkedNode : graph[nodeIndex]){
                if(!visited[LinkedNode]){
                    stack.push(LinkedNode);
                    visited[LinkedNode]=true;
                }
            }
        }
    }
}