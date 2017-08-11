from pybrain.datasets import SupervisedDataSet
DS = SupervisedDataSet( 16, 26 )
DS.appendLinked( [1,2,3], [4,5] )
len(DS)
1
