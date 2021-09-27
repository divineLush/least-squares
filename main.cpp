#include <iostream>
#include <omp.h>

int main() {
    const double points[5][2] = {
        {1, 5.3},
        {2, 6.3},
        {3, 4.8},
        {4, 3.8},
        {5, 3.3}
    };

    double sumx = 0;
    double sumy = 0;
    double sumxdouble = 0;
    double sumxy = 0;

    int i;
    int const len = sizeof(points) / sizeof(points[0]);

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
    } else {
        std::cout << "no solution" << '\n';
    }

    return 0;
}
