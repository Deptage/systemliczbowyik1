model=keras.Sequential([
    keras.layers.Dense(1000,activation='relu',input_shape=(18,)),
    keras.layers.Dense(1000,activation='relu'),
    keras.layers.Dense(1000,activation='relu'),
    keras.layers.Dense(1000,activation='relu'),
    keras.layers.Dense(1000,activation='relu'),
    keras.layers.Dense(100,activation='relu'),
    keras.layers.Dense(100,activation='relu'),
    keras.layers.Dense(100,activation='relu'),
    keras.layers.Dense(100,activation='relu'),
    keras.layers.Dense(1),
])
model.summary()

model.compile(optimizer='adam',loss=keras.losses.MeanSquaredError(),metrics=['accuracy'])
early_stopping_monitor = EarlyStopping(monitor='val_loss', patience=20, restore_best_weights=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4,random_state=1697) 
trening=model.fit(X_train,y_train,epochs=3000,validation_split=0.3,callbacks=[early_stopping_monitor],batch_size=4)
