# mathematical

This repo, which was created just for fans, is currently going to cover a series of algorithmic topics that have a mathematical base. For example Lagrange polynomial interpolation and Graham algorithm for convex hull.
Oh, I was forgetting. We are going to write program with **Julia** and hands on with that. So let's go.

### Lagrange Polynomial Interpolation

The file `lagrange_interpolation.jl` provides a Julia implementation for Lagrange Polynomial Interpolation. The script prompts the user to input the number of points and the corresponding x and y values. It then calculates the Lagrange interpolation polynomial and visualizes the result using the Plots library.

##### Usage

+ Make sure you have Julia and the Plots library installed.
+ Run the script: julia `lagrange_interpolation.jl`
+ Enter the number of points and the x, y values as prompted.

### Convex Hull

The file convex_hull.jl contains a Julia implementation for finding the convex hull of a set of points using the Graham's scan algorithm. The script prompts the user to input the number of points and the coordinates. It then calculates the convex hull and visualizes the result using the Plots library.

##### Usage

+ Make sure you have Julia and the Plots library installed.
+ Run the script: `julia convex_hull.jl`
+ Enter the number of points and the x, y values as prompted.

### Notes

+ The Plots library is used for visualization. Ensure it is installed before running the scripts.
+ Both scripts contain user prompts for input, providing an interactive experience.
+ The resulting plots will be displayed, illustrating the Lagrange Polynomial Interpolation or the Convex Hull, depending on the script executed.

Feel free to explore, use, and modify these scripts for your needs. If you have any questions or suggestions, please open an issue or pull request. Happy coding!

