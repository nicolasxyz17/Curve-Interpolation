#%%

# MIT License

# Copyright (c) 2020 Hernan Reisin

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import matplotlib.pyplot as plt
import numpy as np


class data:
    timeToMaturity = [0.57,0.84,0.88,1.47,1.75,1.95,2.31,2.42,3.34,4.26,4.75,5.3 ,6.43,10.99]
    yieldSep17     = [0.48,0.15,0.25,1.51,2.69,2.55,4.93,3.49,4.31,5.26,5.69,5.76,6.04,7.53]
    
def plotTermStructures():
    plt.plot(data.timeToMaturity,data.yieldSep17,marker='.',markersize=10,color='skyblue',linewidth=1,label='17.SEP.2020')
    plt.legend()
    
def main():  
    plotTermStructures()
    
    
if __name__ == "__main__": 
    main()