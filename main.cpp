#include <iostream>
#include <typeinfo>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <omp.h>

// g++ -fopenmp main.cpp -o main

int main() {
    std::ifstream input ("input.csv");
    std::vector<std::vector<int>> points;

    // read from input.csv
    if (input.is_open()) {
        std::string line;

        while(std::getline(input, line)) {
            std::size_t pos = line.find(",");

            int x = std::stoi(line.substr(0, pos));
            int y = std::stoi(line.substr(pos + 1));

            points.push_back({ x, y });
        }
    }
    input.close();


    double sumx = 0;
    double sumy = 0;
    double sumxdouble = 0;
    double sumxy = 0;

    int i;
    const int len = points.size();

    #pragma omp parallel for private(i) reduction(+:sumx, sumy, sumxy, sumxdouble)
        for (i = 0; i < len; i++) {
            sumx += points[i][0];
            sumy += points[i][1];
            sumxdouble += points[i][0] * points[i][0];
            sumxy += points[i][0] * points[i][1] ;
        }

    double const det = sumxdouble * len - sumx * sumx;

    if (det != 0) {
        double const deta = sumxy * len - sumx * sumy;
        double const a = deta / det;

        double const detb = sumxdouble * sumy - sumxy * sumx;
        double const b = detb / det;

        std::cout << a << " " << b << '\n';

        std::ofstream output ("output.csv");
        if (output.is_open()) {
            output << a << "," << b << "\n";
        }
        output.close();

    } else {
        std::cout << "no solution" << '\n';
    }

    return 0;
}
