
1. 首先定义了一个参数OGR（过拟合-泛化比），$O_N$代表模型的过拟合程度，$G_N$代表模型的泛化能力。我们希望$O_N$尽可能小，$G_N$尽可能大，也就是希望OGR尽可能小。

$$
OGR = | \frac{\Delta O_{N,n}}{\Delta G_{N,n}} |
$$

2. 直接计算OGR存在一些问题，如何计算泛化误差？训练误差计算一次时间太长，因此我们无法直接优化这个目标，因此作者将其转换成解决一个**无穷小问题**，作者将其转化为最小化$OGR^2$，也就是想要让每一步更新都要让泛化误差(验证集上的损失)的提升尽可能小，对于多模态场景来说，就是需要将多个模态的更新加起来让$OGR^2$最小
3. 因此在更新过程中使用一阶近似我们可以得到：

$$
OGR^2 = (\frac{\langle \mathcal{L^T}-\nabla \mathcal{L}^*,g \rangle }{\langle \nabla\mathcal{L}^*,g \rangle})^2
$$

4. 由于$g$是由多个模态的梯度组成的，因此可以把$g$写成累加的形式

$$
OGR^2 = (\frac{\langle \mathcal{L^T}-\nabla \mathcal{L}^*,\sum_k \omega_k v_k \rangle }{\langle \nabla\mathcal{L}^*, \sum_k \omega_k v_k\rangle})^2
$$

5. 我们要求得最优的$\omega^*$，使得这个式子最小，这个式子存在最优解：

$$
\omega_k^*=\frac{1}{Z}\frac{\langle \nabla\mathcal{L}^*,v_k \rangle}{\sigma_k^2}, \text{where}~\sigma_k^2\equiv\mathbb{E}[\langle \nabla\mathcal{L^T}-\nabla\mathcal{L}^*,v_k \rangle^2]~and~Z=\sum_k\frac{\langle \nabla\mathcal{L}^*,v_k \rangle}{2\sigma_k^2}
$$

6. 因此我们就可以通过这个式子计算出最后的$\omega_k^*$，其中$\nabla\mathcal{L}^*$又验证集中的一小部分来估计。
