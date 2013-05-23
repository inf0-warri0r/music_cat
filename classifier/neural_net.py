"""
Author : tharindra galahena (inf0_warri0r)
Project: classifing music using neural network
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 23/05/2013
License:

     Copyright 2013 Tharindra Galahena

This is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. This is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
this. If not, see http://www.gnu.org/licenses/.

"""

import math
import random


class node:

    def __init__(self, inp):

        self.num_inputs = inp
        self.weights = list()
        self.inputs = list()
        self.errors = list()
        self.output = 0.0


class layer:

    def __init__(self, nn):

        self.num_nodes = nn
        self.chr = list()


class neural:

    def __init__(self, inp, out, num, hn, lr, mm):

        self.layers = list()
        self.weights = list()
        self.num_inputs = inp
        self.num_outputs = out
        self.num_layers = num
        self.num_hid_nodes = hn
        self.num_weights = 0
        self.learning_rate = lr
        self.momen = mm

        l_in = layer(inp)

        for i in range(0, self.num_inputs):
            tmp = node(1)
            l_in.chr.append(tmp)
            self.num_weights = self.num_weights + 1

        self.layers.append(l_in)

        for i in range(1, self.num_layers - 1):

            ltmp = layer(self.num_hid_nodes)
            nd = self.layers[i - 1].num_nodes

            for j in range(0, hn):
                tmp = node(nd + 1)
                ltmp.chr.append(tmp)
                self.num_weights = self.num_weights + nd + 1

            self.layers.append(ltmp)

        nd = self.layers[self.num_layers - 2].num_nodes
        l_out = layer(self.num_outputs)

        for i in range(0, self.num_outputs):
            tmp = node(nd + 1)
            l_out.chr.append(tmp)
            self.num_weights = self.num_weights + nd + 1

        self.layers.append(l_out)

    def init(self):

        for i in range(0, self.num_layers):
            for j in range(0, self.layers[i].num_nodes):
                for k in range(0, self.layers[i].chr[j].num_inputs):
                    r = random.uniform(-1.0, 1.0)
                    self.layers[i].chr[j].weights.append(r)
                    self.layers[i].chr[j].errors.append(r)
                    self.layers[i].chr[j].inputs.append(r)
                    self.weights.append(random.uniform(-1.0, 1.0))

    def get_num_weights(self):

        return self.num_weights

    def get_weights(self):

        n = 0
        for i in range(0, self.num_layers):
            for j in range(0, self.layers[i].num_nodes):
                for k in range(0, self.layers[i].chr[j].num_inputs):
                    self.weights[n] = self.layers[i].chr[j].weights[k]
                    n = n + 1
        return self.weights

    def put_weights(self, weights):

        n = 0
        for i in range(0, self.num_layers):
            for j in range(0, self.layers[i].num_nodes):
                for k in range(0, self.layers[i].chr[j].num_inputs):
                    self.layers[i].chr[j].weights[k] = weights[n]
                    n = n + 1

    def update(self, inputs):

        outputs = list()

        for i in range(0, self.num_layers):
            outputs = list()
            if i == 0:
                sm = 0.0

                for j in range(0, self.layers[i].num_nodes):
                    self.layers[i].chr[j].inputs[0] = inputs[j]
                    sm = sm + self.layers[i].chr[j].weights[0] * inputs[j]
                    sm = self.convert(sm)
                    self.layers[i].chr[j].output = sm
                    outputs.append(sm)
            else:
                for j in range(0, self.layers[i].num_nodes):
                    sm = 0.0

                    for k in range(0, self.layers[i].chr[j].num_inputs - 1):
                        self.layers[i].chr[j].inputs[k] = inputs[k]
                        sm = sm + self.layers[i].chr[j].weights[k] * inputs[k]

                    index = self.layers[i].chr[j].num_inputs - 1
                    self.layers[i].chr[j].inputs[index] = -1.0
                    sm = sm - self.layers[i].chr[j].weights[index]
                    sm = self.convert(sm)
                    self.layers[i].chr[j].output = sm
                    outputs.append(sm)

            inputs = outputs

        return outputs

    def get_weighted_error(self, l, inp):
        sm = 0.0
        for j in range(0, self.layers[l].num_nodes):
            error = self.layers[l].chr[j].errors[inp]
            weight = self.layers[l].chr[j].weights[inp]
            sm = sm + error * weight

        return sm

    def learn(self, dout):
        tmp = self.num_layers - 1
        for j in range(0, self.layers[tmp].num_nodes):
            dalta = self.layers[tmp].chr[j].output
            dalta = dalta * (1.0 - self.layers[tmp].chr[j].output)
            dalta = dalta * (dout[j] - self.layers[tmp].chr[j].output)

            for k in range(0, self.layers[tmp].chr[j].num_inputs):
                err = dalta + self.momen * self.layers[tmp].chr[j].errors[k]
                self.layers[tmp].chr[j].errors[k] = err
                upd = self.learning_rate
                upd = upd * self.layers[tmp].chr[j].inputs[k] * err
                upd = self.layers[tmp].chr[j].weights[k] + upd
                self.layers[tmp].chr[j].weights[k] = upd

        i = self.num_layers - 2
        while i >= 0:
            for j in range(0, self.layers[i].num_nodes):
                sm = self.get_weighted_error(i + 1, j)
                for k in range(0, self.layers[i].chr[j].num_inputs):

                    dalta = self.layers[i].chr[j].output
                    dalta = dalta * (1 - self.layers[i].chr[j].output) * sm
                    err = dalta + self.momen * self.layers[i].chr[j].errors[k]
                    self.layers[i].chr[j].errors[k] = err
                    upd = self.learning_rate
                    upd = upd * self.layers[i].chr[j].inputs[k]
                    upd = upd * self.layers[i].chr[j].errors[k]
                    upd = upd + self.layers[i].chr[j].weights[k]
                    self.layers[i].chr[j].weights[k] = upd
            i = i - 1

    def convert(self, value):
        #print value
        return (1.0 / (1.0 + math.exp(-1.0 * value)))
