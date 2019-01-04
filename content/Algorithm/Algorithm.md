[TOC]





# Algorithm

>  在编程领域中，不成熟的优化是所有的罪恶之源

## 重要的问题类型

排序、查找、字符串处理、图问题、组合问题、几何问题、数值问题

### 大整数乘法



## 基本数据结构

线性数据结构、图、树、集合与字典

## selection problem

一个长度为N的数组中，找出第k个最大值。

## 递归的四条基本法则

1. 基本情景。必须存在不用递归就能解出的基本情景

2. 不断推进。每次递归都必须使状态朝向一种基准情形推进

3. 设计法则。假设所有的递归调用都能运行

4. 合成效益法则。在求解一个问题的同一实例时，切勿在不同的递归中做重复性工作。

```java
public static long fib(int n) {
    if(n <= 1) {
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
}
```

该结构的递归效率相当低



## 表、栈和队列

abstract data type, ADT

### 常见操作

printList、makeEmpty

insert、remove、findKth

next、previous

## 树

1. 先序历遍：目录打印
2. 中序历遍：表达式
3. 后续历遍：统计目录大小

### 查找树ADT-二叉查找树

$$
x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$



### AVL树

#### 单旋转

#### 双旋转

### B树
## 散列

### 分离链接法

将散列到同一个值的所有元素保存到一个表中。除链表外，任何方案都可以冲突现象；一颗二叉查找树甚至另一个散列都将胜任这个工作。但是，我们期望散列表是大的并且散列函数是好的，那么所有的链表是短的，从而任何复杂的尝试就不值得考虑了。

### 不用链表的散列表



## 优先队列

### 二叉堆



## 排序

### 选择排序

> 命题A：对于长度为N的数组，选择排序需要大约$N^2/2$次比较和N次交换。
>
> 证：每次交换前需要在未排序的序列(N-i)中找到最大值，需要N-i-1次比较和1次交换。
>
> 比较次数
> $$
> (N-1) +(N-2)+\dots+2+1=N(N-1)/2\sim N^2
> $$
> 交换次数为
> $$
> N-1\sim N
> $$
>

* 运行时间与输入无关：输入一个有序，或者主键全部相等的数组和元素随机排列的数组所用的时间是一样的。

* 数据移动是最少的：选择排序只用了N次交换；

```java
private boolean less(T v, T w) {
    return v.compareTo(w) < 0;
}

private void exch(T[] a, int i, int j) {
    T t = a[i];
    a[i] = a[j];
    a[j] = t;
}

public boolean isSorted(T[] a) {
    for (int i = 1; i < a.length; i++) {
        if (less(a[i], a[i-1])) {
            return false;
        }
    }
    return true;
}

public void selectSort(T[] a) {
    int N = a.length;
    for (int i = 0; i < N; i++) {
        int min = i;
        for (int j = i+1; j < N; j++) {
            if (less(a[i], a[min])) {
                min = j;
            }
        }
        exch(a, i , min);
    }
}
```



### 插入排序     

> 命题A：对于随机排列长度为N且主键不重复的数组，平均情况下插入排序需要$\sim N^2/4$次比较以及$\sim N^2/4$次交换。最坏境况下需要$\sim N^2/2$次比较和$\sim N^2/2$次交换，最好的情况下需要$N-1$次比较和0次交换。



```java
void insertionSort(T[] a) {
    int j;
	for (int p = 1; p < a.length; p++) {
        T tmp = a[p];
        for (j = p; j >0 && tmp.compareTo(a[j-1]) < 0; j--) {
            a[j] = a[j-1];
        }
        a[j] = tmp;
    }
}	
```
### 希尔排序

```java
void shellsort(int[] a) {
    int j;
    for (int gap = a.length / 2; gap >0; gap/=2) {
        for (int i = gap; i < a.length; i++) {
            int tmp = a[i];
            for (j = i; j >= gap && Integer.compare(tmp, a[j-gap]) < 0; j -= gap) {
                a[j] = a[j-gap];
            }
            a[j] = tmp;
        }
    }
}
```



### 堆排序

1. 建立二叉堆 O(N)
2. 执行N次deleteMin单个花费时间O(logN)
3. 将N个元素记录到另外一个数组上，然后将数组拷贝回来

缺点：需要增加一倍的存储。

堆排序是一个非常稳定的算法：它使用的平均只比最坏情景边界略少



```java
void heapsort(T[] a) {
    for (int i = a.length/2-1; i >= 0; i--) {
        percDown(a, i, a.length);
    }
    for (int i = a.length-1; i>0; i--) {
        swapReferences(a, 0, i);
        percDown(a, 0, i);
    }
}

private void swapReferences(T[] a, int i, int j) {
    T tmp = a[i];
    a[i] = a[j];
    a[j] = tmp;
}

private int leftChild(int i) {
    return 2*i+1;
}

private void percDown(T[] a, int i, int n) {
    int child;
    T tmp;

    for (tmp = a[i]; leftChild(i) < n; i= child) {
        child = leftChild(i);
        if (child != n-1 && a[child].compareTo(a[child+1]) < 0) {
            child++;
        }
        if (tmp.compareTo(a[child]) < 0) {
            a[i] = a[child];
        } else {
            break;
        }
    }
    a[i] = tmp;
}
```



### 归并排序

归并排序以O(NlogN)最坏情景时间运行，而所用的比较次数几乎是最优的。它是递归算法一个好的实例。归并排序的运行时间严重依赖比较元素和在数组中移动元素的开销。这些开销是与语言相关的。在java中进行一次元素比较可能是昂贵的（因为比较可能不容易被内嵌，动态调用的开销会减慢执行速度），但移动元素是省时的（因为他们是引用的赋值，而不是庞大的对象的拷贝）

归并排序使用所有流行的排序中最少的比较次数。它是标准Java类库中泛型排序所使用的算法。

另一方面，在C++的泛型排序中，如果对象庞大，那么拷贝对象可能需要很大开销，而编译器具有主动执行内嵌优化的能力，比较对象常常是相对省时的。Quicksort则能达到该种平衡，并且是C++库的通常所使用的排序例程。

在Java中，快速排序也用作基本类型的标准库排序。这里，比较和数据移动的开销是类似的，因此使用少得多的数据移动足以补偿那些附加的比较而且还有盈余。

```java
void mergeSort(int[] a, int[] temArray, int left, int right) {
    if (left < right) {
        int center = (left + right) / 2;
        mergeSort(a, temArray, left, center);
        mergeSort(a, temArray, center + 1, right);
        merge(a, temArray, left, center+1, right);
    }
}

public void mergeSort(int[] a) {
    int[] tmpArray = new int[a.length];
    mergeSort(a, tmpArray, 0, a.length - 1);
}

void merge(int[] a, int[] tmpArray, int leftPos, int rightPos, int rightEnd) {
    int leftEnd = rightPos - 1;
    int tmpPos = leftPos;
    int numElements = rightEnd - leftPos + 1;

    while (leftPos <= leftEnd && rightPos <= rightEnd){
        if (Integer.compare(a[leftPos], a[rightPos]) <= 0) {
            tmpArray[tmpPos++] = a[leftPos++];
        } else {
            tmpArray[tmpPos++] = a[rightPos++];
        }
    }

    while (leftPos <= leftEnd) {
        tmpArray[tmpPos++] = a[leftPos++];
    }

    while (rightPos <= rightEnd) {
        tmpArray[tmpPos++] = a[rightPos++];
    }

    for (int i = 0; i < numElements; i++, rightEnd--) {
        a[rightEnd] = tmpArray[rightEnd];
    }
}
```

### 快速排序


​            

```java
public static void sort(List<Integer> items) {
	if (items.size() > 1) {
        List<Integer> smaller = new ArrayList<>();
        List<Integer> same = new ArrayList<>();
        List<Integer> larger = new ArrayList<>();
        Integer chosenItem = items.get(items.size()/2);        
        for (Integer i : items) {
            if (i < chosenItem) {
                smaller.add(i);
            } else if (i > chosenItem) {
                larger.add(i);
            } else {
                same.add(i);
            }
        }
        sort(smaller);
        sort(larger);
        items.clear();
        items.addAll(smaller);
        items.addAll(same);
        items.addAll(larger);
    }
}
```
> 快速排序的策略
>
> * 选择枢纽元：三数中值分割法

```java
T median3(T[] a, int left, int right) {
    int center = (left + right) / 2;

    if (a[center].compareTo(a[left]) < 0) {
        swapReferences(a, left, center);
    }
    if (a[right].compareTo(a[left]) < 0) {
        swapReferences(a, left, right);
    }
    if (a[right].compareTo(a[center]) < 0) {
        swapReferences(a, center, right);
    }

    swapReferences(a, center, right-1);
    return a[right-1];
}
```

为了交换动作的速度，有时需要将swapReferences显式的写出。强制使编译器以直接插入的方式编译这些代码。如果swapReferences是final方法，则大多数编译器都将自动这么做，但对于不这么做的编译器，差别可能会很明显。

> * 分割策略：左小右大位置交替策略

```java
void quickSort(T[] a, int left, int right) {
    if (left + CUTOFF <= right) {
        T pivot = median3(a, left, right);

        int i = left, j = right - 1;
        for (;;) {
            while (a[++i].compareTo(pivot) < 0) {}
            while (a[--j].compareTo(pivot) > 0) {}
            if (i < j) {
                swapReferences(a, i, j);
            } else {
                break;
            }
        }
        swapReferences(a, i, right-1);

        quickSort(a, left, i-1);
        quickSort(a, i+1, right);
    } else {
        insertionSort(a, left, right);
    }
}
```

#### 快速选择

```java
void quickSelect(T[] a, int left, int right, int k) {
    if (left + CUTOFF <= right) {
        T pivot = median3(a, left, right);

        int i = left, j = right - 1;
        for (;;) {
            while (a[++i].compareTo(pivot) < 0) {}
            while (a[--j].compareTo(pivot) > 0) {}
            if (i < j) {
                swapReferences(a, i, j);
            } else {
                break;
            }
        }
        swapReferences(a, i, right-1);

        if (k <= i) {
            quickSelect(a, left, i-1, k);
        } else if (k > i + 1) {
            quickSelect(a, i+1, right, k);
        }
    } else {
        insertionSort(a, left, right);
    }
}
```

### 排序算法的一般下界

> 引理：令T是深度为d的二叉树，则T最多有$2^d$片树叶
>
> 引理：具有L片树叶的二叉树的深度至少是$ \left \lceil \log{L} \right \rceil $ 。
>
>  定理：只使用元素间的比较的任何排序算法在最差的情况下至少需要$ \left \lceil \log{N!} \right \rceil $次比较
>
> 定理：只使用元素间的比较的任何排序算法均需要$\Omega(N\log{N})$次比较
> $$
> \begin{align*}
> \log{N!}&= \log(N(N-1)(N-2)\dots(2)(1))\\
> 		&=\log{N}+\log{N-1}+\log{N-2}+\dots+\log{2}+\log{1}\\
> 		&\ge\log{N}+\log{N-1}+\log{N-2}+\dots+\log{N/2}\\
> 		&\ge\frac{N}{2}\log{\frac{N}{2}}\ge\frac{N}{2}\log{N}-\frac{N}{2}=\Omega(N\log{N})\\
> \end{align*}
> $$
>


$$
X=\left|
	\begin{matrix}
		x_{11} & x_{12} & \cdots & x_{1d}\\
		x_{21} & x_{22} & \cdots & x_{2d}\\
		\vdots & \vdots & \ddots & \vdots \\
		x_{11} & x_{12} & \cdots & x_{1d}\\
	\end{matrix}
\right|
$$


### 线性时间的排序：桶排序和基数排序

```java
void radixSortA(String[] arr, int stringLen) {
    final int BUCKETS = 256;
    ArrayList<String>[] buckets = new ArrayList[BUCKETS];
    
    for (int i = 0; i < BUCKETS; i++) {
        buckets[i] = new ArrayList<>();
    }
    
    for (int pos = stringLen - 1; pos >= 0; pos--) {
        for (String s:arr) {
            buckets[s.charAt(pos)].add(s);
        }
        int idx = 0;
        
        for (ArrayList<String> thisBucket:buckets) {
            for (String s:thisBucket) {
                arr[idx++] = s;
            }
            
            thisBucket.clear();
        }
    }
}
```

字符串的基数排序



### 外部排序

### 总结

对于大部分一般的内部排序的应用，选用的方法不是插入排序、希尔排序、归并排序就是快速排序，这主要是有输入及底层环境来决定的。插入排序使用于非常少量的输入。对于中等规模的输入，希尔排序是一个不错的选择。只要增量序列合适，它可以用少量代码就给出优异的表现。归并排序最差的环境下的表现为O(NlogN)，但是需要额外的空间。然而，它用到的比较次数近乎是最优的，因为任何仅用元素比较来进行排序的算法都会对某些输入序列必须用至少$ \left \lceil \log{N!} \right \rceil $次比较。快速排序自己并不保证提供这种最坏时间的复杂度，并且编程比较麻烦。但是，它可以几乎肯定地做到O(NlogN)，并且跟堆排序组合在一起就可以保证最坏情景下有O(NlogN)。用基数平排序可以将字符串在线性时间内排序，这在某些情况下是対相对于基于比较的排序而言更实际的另一种选择。

## 不相交集类

### 等价关系



## 图论算法

### 拓扑排序



### 最短路径算法

### 网络流问题

### 最小生成树

### 深度优先搜索

### NP-完全性介绍

## 动态规划

> 钢条切割问题：

```
CUT-ROD(p, n) 
	if n==0
		return 0
	q = -inf
	for i = 1 to n
		q = max(q,p[i]+CUT-ROD(p, n-i))
```



## 算法设计技巧

### 贪婪算法

### 回溯算法

### 最大子数组

 

## 摊还分析

## 高级数据结构及实现










