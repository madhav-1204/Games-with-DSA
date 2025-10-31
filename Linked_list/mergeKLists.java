import java.util.LinkedList;
import java.util.Scanner;

class Point {
    int x, y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class SnakeGame {
    static final int SIZE = 10;  // grid size (10x10)
    static LinkedList<Point> snake = new LinkedList<>();
    static Point food = new Point(5, 5);

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Initialize snake (3 segments)
        snake.add(new Point(0, 0));
        snake.add(new Point(0, 1));
        snake.add(new Point(0, 2));

        System.out.println("=== Snake Move Game ===");
        System.out.println("Controls: W = Up, S = Down, A = Left, D = Right, Q = Quit");

        while (true) {
            printBoard();

            System.out.print("Move: ");
            char move = sc.next().toUpperCase().charAt(0);

            if (move == 'Q') {
                System.out.println("Game Over! You quit.");
                break;
            }

            if (!moveSnake(move)) {
                System.out.println("You hit the wall! Game Over.");
                break;
            }
        }
        sc.close();
    }

    static boolean moveSnake(char dir) {
        Point head = snake.getLast();
        int newX = head.x;
        int newY = head.y;

        switch (dir) {
            case 'W': newX--; break; // up
            case 'S': newX++; break; // down
            case 'A': newY--; break; // left
            case 'D': newY++; break; // right
            default: System.out.println("Invalid move! Use W/A/S/D."); return true;
        }

        // check boundaries
        if (newX < 0 || newX >= SIZE || newY < 0 || newY >= SIZE)
            return false;

        Point newHead = new Point(newX, newY);
        snake.addLast(newHead);

        // if snake eats food, don't remove tail
        if (newX == food.x && newY == food.y) {
            System.out.println("Yum! You ate the food!");
            food = new Point((int)(Math.random() * SIZE), (int)(Math.random() * SIZE));
        } else {
            snake.removeFirst(); // move by removing tail
        }
        return true;
    }

    static void printBoard() {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                boolean isSnake = false;
                for (Point p : snake) {
                    if (p.x == i && p.y == j) {
                        System.out.print("S ");
                        isSnake = true;
                        break;
                    }
                }
                if (!isSnake) {
                    if (food.x == i && food.y == j)
                        System.out.print("F ");
                    else
                        System.out.print(". ");
                }
            }
            System.out.println();
        }
        System.out.println();
    }
}
