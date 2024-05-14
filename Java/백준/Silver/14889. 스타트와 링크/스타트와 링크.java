import java.io.*;
import java.util.*;

class Team {
    public ArrayList<Integer> Members = new ArrayList<>();
    public int score = 0;
    public HashMap<Integer,Integer> member2score = new HashMap<>(); 
    public int[][] scoreTable;
    Team (int[][] scoreTable) {
        this.scoreTable = scoreTable;
    }

    public void addMember(Integer member) {
        int thisScore = 0;
        for (int i = 0; i < Members.size(); i++) {
            int another = Members.get(i);
            thisScore += this.scoreTable[member][another];
            thisScore += this.scoreTable[another][member];
        }
        this.Members.add(member);
        member2score.put(member, thisScore);
        this.score += thisScore;
    }

    public void removeLastMember() {
        int lastMember = this.Members.get(this.size() - 1);
        this.Members.remove(this.size() - 1);
        this.score -= member2score.get(lastMember);
        member2score.remove(lastMember);
    }

    public int size() {
        return this.Members.size();
    }
}

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static Team teamA, teamB;
    static int pickableCount;
    static int minDiff = Integer.MAX_VALUE;
    static int N;
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        pickableCount = N / 2;
        int[][] scoreTable = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0 ; j < N; j++) scoreTable[i][j] = Integer.parseInt(st.nextToken());
        }

        teamA = new Team(scoreTable);
        teamB = new Team(scoreTable);
        backtracking(0);
        System.out.println(minDiff);
    }

    static void backtracking(int depth) {
        if (depth == N) {
            int diff = absDiff(teamA.score, teamB.score);
            if (minDiff > diff) minDiff = diff;
        }
        else {
            // put thisman into teamA if that able
            if (teamA.size() < pickableCount) {
                teamA.addMember(depth);
                backtracking(depth + 1);
                teamA.removeLastMember();
            }

            if (teamB.size() < pickableCount) {
                teamB.addMember(depth);
                backtracking(depth + 1);
                teamB.removeLastMember();
            }
        }
    }

    static int absDiff(int a, int b) {
        if (a > b) return a - b;
        else return b - a;
    }
}
