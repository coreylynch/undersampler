class UnderSampler(BaseEstimator):
"""Undersamples unbalanced datasets to make the classes the same size.
""" 
    def fit(self, y, shuffle=True):
        """Builds an index of similarly proportioned classes by randomly
        undersampling the majority class.

        Parameters
        ----------
        X : array-like shape [n_samples, n_features]
        """
        counter = Counter(y)
        num_neg = counter[counter.keys()[0]]
        num_pos = counter[counter.keys()[1]]

        n_samples = len(y)

        positives = []
        negatives = []
        for i in range(n_samples):
            if y[i] > 0:
                positives.append(i)
            else:
                negatives.append(i)
        counter_samples = []
        if num_neg > num_pos:
            for i in range(len(positives)):
                counter_samples.append(np.random.randint(len(negatives)))
                self.balanced_index = np.concatenate((positives,counter_samples))
        else:
            for i in range(len(negatives)):
                counter_samples.append(np.random.randint(len(positives)))
                self.balanced_index = np.concatenate((negatives,counter_samples))
        if shuffle is True:
            index = np.arange(0,len(self.balanced_index))
            np.random.shuffle(index)
            self.balanced_index = self.balanced_index[index]
        return self

    def transform(self, X, y):
        X = X[self.balanced_index]
        y = y[self.balanced_index]
        return X, y

    def fit_transform(self, X, y=None, **fit_params):
        """Fit to data, then transform it

        Fits transformer to X and y with optional parameters fit_params
        and returns a transformed version of X.

        Parameters
        ----------
        X : numpy array of shape [n_samples, n_features]
            Training set.

        y : numpy array of shape [n_samples]
            Target values.

        Returns
        -------
        X_new : numpy array of shape [n_samples, n_features_new]
            Transformed array.

        """
        return self.fit(X, y, **fit_params).transform(X,y)