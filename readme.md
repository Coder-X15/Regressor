## Regressor : Regression Line Builder

The command line tool can be used to obtain the regression coefficients (m, c) of the regression line y = mx+ c for a particular dataset. The usage is:
``` python3 <or python> regressor.py /path/to/csv/dataset ```

or, if you can compile the same using `pyinstaller` and add the path of the executable present in the resultant folder `dist` to the PATH environment variable (Linux users may export the path), use it like:
``` regressor /path/to/csv/dataset ```

The tool uses Ordinary Least Squares (OLS) method to obtain the coefficients instead of using `sklearn.linear_model.LinearRegression` thus making the code look very basic and yet useful (maybe not worth adding since `sklearn` is what that is quite popular among data scientists and ML engineers, but I'm just trying to make stuff out of my learning sessions at my Institute and at home :) ) 
