## 我为什么选择了Python

目前，Python语言的发展势头在国内国外都是不可阻挡的，Python凭借其简单优雅的语法，强大的生态圈从众多语言中脱颖而出，如今已经是稳坐编程语言排行榜前三的位置。国内很多Python开发者都是从Java开发者跨界过来的，我自己也不例外。我简单的跟大家交代一下，我为什么选择了Python。

### Python vs. Java

我们通过几个例子来比较一下，做同样的事情Java和Python的代码都是怎么写的。

例子1：在终端中输出“hello, world”。

Java代码：

```Java
class Test {
	
    public static void main(String[] args) {
        System.out.println("hello, world");
    }
}
```

Python代码：

```Python
print('hello, world')
```

例子2：从1到100求和。

Java代码：

```Java
class Test {
    
    public static void main(String[] args) {
        int total = 0;
        for (int i = 1; i <= 100; i += 1) {
            total += i;
        }
        System.out.println(total);
    }
}
```

Python代码：

```Python
print(sum(range(1, 101)))
```

例子3：双色球随机选号。

Java代码：

```Java
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Test {

    /**
     * 产生[min, max)范围的随机整数
     */
    public static int randomInt(int min, int max) {
        return (int) (Math.random() * (max - min) + min);
    }

    public static void main(String[] args) {
        // 初始化备选红色球
        List<Integer> redBalls = new ArrayList<>();
        for (int i = 1; i <= 33; ++i) {
            redBalls.add(i);
        }
        List<Integer> selectedBalls = new ArrayList<>();
        // 选出六个红色球
        for (int i = 0; i < 6; ++i) {
            selectedBalls.add(redBalls.remove(randomInt(0, redBalls.size())));
        }
        // 对红色球进行排序
        Collections.sort(selectedBalls);
        // 添加一个蓝色球
        selectedBalls.add(randomInt(1, 17));
        // 输出选中的随机号码
        for (int i = 0; i < selectedBalls.size(); ++i) {
            System.out.printf("%02d ", selectedBalls.get(i));
            if (i == selectedBalls.size() - 2) {
                System.out.print("| ");
            }
        }
        System.out.println();
    }
}
```

Python代码：

```Python
from random import randint, sample

# 初始化备选红色球
red_balls = [x for x in range(1, 34)]
# 选出六个红色球
selected_balls = sample(red_balls, 6)
# 对红色球进行排序
selected_balls.sort()
# 添加一个蓝色球
selected_balls.append(randint(1, 16))
# 输出选中的随机号码
for index, ball in enumerate(selected_balls):
    print('%02d' % ball, end=' ')
    if index == len(selected_balls) - 2:
        print('|', end=' ')
print()
```

相信，看完这些例子后，你一定感受到了我选择了Python是有道理的。