import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Test03 {

    /**
     * 产生[min, max)范围的随机整数
     */
    public static int randomInt(int min, int max) {
        return (int) (Math.random() * (max - min) + min);
    }

    public static void main(String[] args) {
        List<Integer> redBalls = new ArrayList<>();
        for (int i = 1; i <= 33; ++i) {
            redBalls.add(i);
        }
        List<Integer> selectedBalls = new ArrayList<>();
        for (int i = 0; i < 6; ++i) {
            selectedBalls.add(redBalls.remove(randomInt(0, redBalls.size())));
        }
        Collections.sort(selectedBalls);
        selectedBalls.add(randomInt(1, 17));
        for (int i = 0; i < selectedBalls.size(); ++i) {
            System.out.printf("%02d ", selectedBalls.get(i));
            if (i == selectedBalls.size() - 2) {
                System.out.print("| ");
            }
        }
        System.out.println();
    }
}