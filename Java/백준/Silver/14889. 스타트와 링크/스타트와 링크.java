import java.io.*;
import java.util.*;

class Team {
    public int[] Members;
    public int size = 0;
    public int score = 0;
    public int[] member2score; 
    public int[][] scoreTable;
    Team (int[][] scoreTable, int maxSize) {
        this.scoreTable = scoreTable;
        this.Members = new int[maxSize];
        this.member2score = new int[maxSize];
    }

    public void addMember(Integer member) {
        int thisScore = 0;
        this.Members[this.size] = member;
        

        for (int i = 0; i < this.size; i++) {
            int another = Members[i];
            thisScore += this.scoreTable[member][another];
            thisScore += this.scoreTable[another][member];
        }

        this.member2score[this.size] = thisScore;
        this.size += 1;
        this.score += thisScore;
    }

    public void removeLastMember() {
        this.score -= member2score[this.size - 1];
        this.size -= 1;
    }

    public int size() {
        return this.size;
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

        teamA = new Team(scoreTable, pickableCount + 1);
        teamB = new Team(scoreTable, pickableCount + 1);
        backtracking(0);
        System.out.println(minDiff);
    }

    static void backtracking(int depth) {
        if (depth == N) {
            int diff = Math.abs(teamA.score-teamB.score);
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
}
