#include <time.h>

#include <cmath>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <random>

// Hàm phát sinh mảng dữ liệu ngẫu nhiên
void GenerateRandomData(int a[], int n)
{
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    for (int i = 0; i < n; i++)
        a[i] = std::rand() % n;
}

// Hàm phát sinh mảng dữ liệu ngẫu nhiên
void GeneratePermutation(int a[], int n)
{
    std::mt19937 rng(std::random_device{}());
    std::uniform_int_distribution<int> dist(0, n - 1);

    for (int i = 0; i < n; i++)
        a[i] = i;

    std::shuffle(&a[0], &a[n], rng);
}

// Hàm phát sinh mảng dữ liệu có thứ tự tăng dần
void GenerateSortedData(int a[], int n)
{
    for (int i = 0; i < n; i++)
        a[i] = i;
}


// Hàm phát sinh mảng dữ liệu có thứ tự ngược (giảm dần)
void GenerateReverseData(int a[], int n)
{
    for (int i = 0; i < n; i++)
        a[i] = n - 1 - i;
}


// Hàm phát sinh mảng dữ liệu gần như có thứ tự
void GenerateNearlySortedData(int a[], int n)
{
    for (int i = 0; i < n; i++)
    {
        a[i] = i;
    }
    std::mt19937 rng(std::random_device{}());
    std::uniform_int_distribution<int> dist(0, n - 1);
    for (int i = 0; i < 10; i++)
    {
        int r1 = dist(rng);
        int r2 = dist(rng);
        std::swap(a[r1], a[r2]);
    }
}

// -------------------------------------------------
#define RANDOM_DATA        0
#define SORTED_DATA        1
#define REVERSE_DATA       2
#define NEARLY_SORTED_DATA 3
// -------------------------------------------------

void GenerateData(int a[], int n, int type)
{
    switch (type)
    {
    // ngẫu nhiên
    case RANDOM_DATA: 
        GenerateRandomData(a, n);
        break;
    // có thứ tự
    case SORTED_DATA: 
        GenerateSortedData(a, n);
        break;
    // có thứ tự ngược
    case REVERSE_DATA: 
        GenerateReverseData(a, n);
        break;
    // gần như có thứ tự
    case NEARLY_SORTED_DATA: 
        GenerateNearlySortedData(a, n);
        break;
    default:
        GeneratePermutation(a, n);
    }
}