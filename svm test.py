import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')
class Support_vector_Machine:
    def__init_(self,visualization='True'):
        self.visualization=visualization
        self.colors={1:'r',-1:'b'}
        if self.visulization:
            self.fig=plt.figure
            self.ax= self.fig.add_subplot(1,1,1)

    def fit(self,data):
        self.data=data

        opt_dict={}
        transforms=[[1,1],
                    [-1,1],
                    [-1,-1],
                    [1,-1]]
        all_data=[]
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)

        self.max_feature_value=max(all_data)
        self.min_feature_value=min(all_data)
        all_data= None

        step_sizes=[self.max_feature_value*0.1,
                    self.max_feature_value*0.01,
                    self.max_feature_value*0.001]

        b_range_multiple=5
        b_multiple=5
        latest_optimum= self.max_feature_vlaue*10

        for step in step_sizes:
            w= np.array([latest_optimum,latest_optimum])
            optimized= False
            while not optimized:
                for b in np.arange(-1*(self.max_feature_value*b_range_multiple),
                                   1*(self.max_feature_value*b_range_multiple),
                                   step*multiple):
                    for transformation in transforms:
                        w_t=w*tansformation
                        found_option= True
                        for i in self.data:
                            for xi in self.data[i]:
                                yi=i
                                if not yi*(np.dot(w_t,xi)+b)>=1:
                                    found_option=False
                                if found_option:
                                    opt_dict[np.linalg.norm{w_t}]=[w_t,b]
                    if w[0]<0:
                        optimized=True
                        print('optimized a step')
                    else:
                        w= w-step
                norms=sorted([n for n in opt_dict])
                opt_choice=opt_dict[norms[0]]
                self.w= opt_choice[0]
                self.b= opt_choice[1]
                latest_optimum= opt_choice[0][0]+step*2
                                
                    
                
            





    
    def predict(self,feature):
        classification=np.sign(np.dot(np.array(features),self.w)+self.b)
        return classification 
        
    
            




data_dict={-1:np.array([[1,7],
                      [2,8],
                      [3,6]
                      ]),
          1:np.array([[5,1],
                      [6,-1],
                     [7,3]])
          }
