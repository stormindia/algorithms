/*
https://coursera.cs.princeton.edu/algs4/assignments/percolation/specification.php
*/

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;


public class PercolationStats {

    private double[] percolationThresholds;
    private double confidence95 = 1.96;

    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException();
        }
        percolationThresholds = new double[trials];
        for (int i = 0; i < trials; i++) {
            Percolation percolation = new Percolation(n);
            while (!percolation.percolates()) {
                int row = StdRandom.uniformInt(1, n + 1);
                int col = StdRandom.uniformInt(1, n + 1);
                percolation.open(row, col);
            }
            double percolationThreshold = (double) percolation.numberOfOpenSites() / n;
            percolationThresholds[i] = percolationThreshold;
        }

    }

    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(percolationThresholds) / percolationThresholds.length;
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(percolationThresholds) / (percolationThresholds.length - 1);
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        return mean() - confidence95 * stddev() / Math.sqrt(percolationThresholds.length);
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return mean() + confidence95 * stddev() / Math.sqrt(percolationThresholds.length);
    }


    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);
        PercolationStats percolationStats = new PercolationStats(n, trials);
        StdOut.println("mean                    = " + percolationStats.mean());
        StdOut.println("stddev                  = " + percolationStats.stddev());
        StdOut.println(
                "95% confidence interval = [" + percolationStats.confidenceLo() + ", "
                        + percolationStats.confidenceHi() + "]");
    }
}
