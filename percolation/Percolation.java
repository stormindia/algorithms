/*
https://coursera.cs.princeton.edu/algs4/assignments/percolation/specification.php
*/

import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

    private int[][][] grid; // [row][col][{open(0)/closed(-1), locationInUFArray}]
    private WeightedQuickUnionUF uf;
    private int virtualTopIndex;
    private int virtualBottomIndex;
    private int numberOfOpenSites;
    private int totalSites;

    // creates n-by-n grid, with all sites initially blocked
    // first index is 1,1
    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("n must be greater than 0");
        }
        totalSites = n;
        uf = new WeightedQuickUnionUF(totalSites * totalSites + 2);
        grid = new int[totalSites + 2][totalSites + 2][2];
        virtualTopIndex = 0; // location in the uf array
        virtualBottomIndex = totalSites + 1; // location in the uf array
        grid[virtualTopIndex][virtualTopIndex] = new int[] { 0, virtualTopIndex };
        grid[virtualBottomIndex][virtualBottomIndex] = new int[] { 0, virtualBottomIndex };

        int ufIndex = 1;
        for (int i = 1; i <= totalSites; i++) {
            for (int j = 1; j <= totalSites; j++) {
                grid[i][j] = new int[] { -1, ufIndex };
                ufIndex++;
            }
        }
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        if (isOpen(row, col)) return;
        grid[row][col][0] = 0;
        numberOfOpenSites++;

        if (isTopRow(row)) {
            uf.union(virtualTopIndex, grid[row][col][1]);
        }
        else if (isBottomRow(row)) {
            uf.union(virtualBottomIndex, grid[row][col][1]);
        }

        int[][] adjacentSites = {
                { row, col - 1 }, { row, col + 1 }, { row - 1, col }, { row + 1, col }
        };
        for (int[] adjacent : adjacentSites) {
            if (isValidCoordinate(adjacent[0], adjacent[1]) && isOpen(adjacent[0],
                                                                      adjacent[1])) {
                uf.union(grid[row][col][1], grid[adjacent[0]][adjacent[1]][1]);
            }
        }
    }

    private boolean isTopRow(int row) {
        if (row == 1) return true;
        return false;
    }

    private boolean isBottomRow(int row) {
        if (row == totalSites) return true;
        return false;
    }

    private boolean isValidCoordinate(int row, int col) {
        if (row < 1 || row > totalSites || col < 1 || col > totalSites) return false;
        return true;
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        if (!isValidCoordinate(row, col)) {
            throw new IllegalArgumentException("invalid coordinate " + row + "," + col);
        }
        return grid[row][col][0] == 0;
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        if (!isValidCoordinate(row, col)) {
            throw new IllegalArgumentException("invalid coordinate " + row + "," + col);
        }
        return uf.find(grid[row][col][1]) == uf.find(virtualTopIndex);
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return numberOfOpenSites;
    }

    // does the system percolate?
    public boolean percolates() {
        return uf.find(virtualTopIndex) == uf.find(virtualBottomIndex);
    }

    public static void main(String[] args) {

    }
}
