x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

def forward(x):
  return x * w;
def loss(x, y):
  y_pred = forward(x)
  return (y_pred - y) * (y_pred - y)
w_list = []
mes_list = []

for w in np.arange(0.0, 4.0, 0.1):
  print('w=', w)
  l_sum = 0
  for x_val, y_val in zip(x_data, y_data):
    y_pred_val = forward(x_val)
    loss_val = loss(x_val, y_val)
    l_sum += loss_val
    print('\t', x_val, y_val, y_pred_val, loss_val)
  w_list.append(w)
  mes_list.append(l_sum / 3)
