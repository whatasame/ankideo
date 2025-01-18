#pragma once

// @generated by torchgen/gen.py from Function.h

#include <ATen/Context.h>
#include <ATen/DeviceGuard.h>
#include <ATen/TensorUtils.h>
#include <ATen/TracerMode.h>
#include <ATen/core/Generator.h>
#include <ATen/core/Reduction.h>
#include <ATen/core/Tensor.h>
#include <c10/core/Scalar.h>
#include <c10/core/Storage.h>
#include <c10/core/TensorOptions.h>
#include <c10/util/Deprecated.h>
#include <optional>



#include <ATen/ops/mkldnn_rnn_layer_backward_ops.h>

namespace at {


// aten::mkldnn_rnn_layer_backward(Tensor input, Tensor weight1, Tensor weight2, Tensor weight3, Tensor weight4, Tensor hx_, Tensor cx_tmp, Tensor output, Tensor hy_, Tensor cy_, Tensor? grad_output, Tensor? grad_hy, Tensor? grad_cy, bool reverse, int mode, int hidden_size, int num_layers, bool has_biases, bool train, bool bidirectional, int[] batch_sizes, bool batch_first, Tensor workspace) -> (Tensor, Tensor, Tensor, Tensor, Tensor, Tensor, Tensor)
inline ::std::tuple<at::Tensor,at::Tensor,at::Tensor,at::Tensor,at::Tensor,at::Tensor,at::Tensor> mkldnn_rnn_layer_backward(const at::Tensor & input, const at::Tensor & weight1, const at::Tensor & weight2, const at::Tensor & weight3, const at::Tensor & weight4, const at::Tensor & hx_, const at::Tensor & cx_tmp, const at::Tensor & output, const at::Tensor & hy_, const at::Tensor & cy_, const ::std::optional<at::Tensor> & grad_output, const ::std::optional<at::Tensor> & grad_hy, const ::std::optional<at::Tensor> & grad_cy, bool reverse, int64_t mode, int64_t hidden_size, int64_t num_layers, bool has_biases, bool train, bool bidirectional, at::IntArrayRef batch_sizes, bool batch_first, const at::Tensor & workspace) {
    return at::_ops::mkldnn_rnn_layer_backward::call(input, weight1, weight2, weight3, weight4, hx_, cx_tmp, output, hy_, cy_, grad_output, grad_hy, grad_cy, reverse, mode, hidden_size, num_layers, has_biases, train, bidirectional, batch_sizes, batch_first, workspace);
}

// aten::mkldnn_rnn_layer_backward.out(Tensor input, Tensor weight1, Tensor weight2, Tensor weight3, Tensor weight4, Tensor hx_, Tensor cx_tmp, Tensor output, Tensor hy_, Tensor cy_, Tensor? grad_output, Tensor? grad_hy, Tensor? grad_cy, bool reverse, int mode, int hidden_size, int num_layers, bool has_biases, bool train, bool bidirectional, int[] batch_sizes, bool batch_first, Tensor workspace, *, Tensor(a!) out0, Tensor(b!) out1, Tensor(c!) out2, Tensor(d!) out3, Tensor(e!) out4, Tensor(f!) out5, Tensor(g!) out6) -> (Tensor(a!), Tensor(b!), Tensor(c!), Tensor(d!), Tensor(e!), Tensor(f!), Tensor(g!))
inline ::std::tuple<at::Tensor &,at::Tensor &,at::Tensor &,at::Tensor &,at::Tensor &,at::Tensor &,at::Tensor &> mkldnn_rnn_layer_backward_out(at::Tensor & out0, at::Tensor & out1, at::Tensor & out2, at::Tensor & out3, at::Tensor & out4, at::Tensor & out5, at::Tensor & out6, const at::Tensor & input, const at::Tensor & weight1, const at::Tensor & weight2, const at::Tensor & weight3, const at::Tensor & weight4, const at::Tensor & hx_, const at::Tensor & cx_tmp, const at::Tensor & output, const at::Tensor & hy_, const at::Tensor & cy_, const ::std::optional<at::Tensor> & grad_output, const ::std::optional<at::Tensor> & grad_hy, const ::std::optional<at::Tensor> & grad_cy, bool reverse, int64_t mode, int64_t hidden_size, int64_t num_layers, bool has_biases, bool train, bool bidirectional, at::IntArrayRef batch_sizes, bool batch_first, const at::Tensor & workspace) {
    return at::_ops::mkldnn_rnn_layer_backward_out::call(input, weight1, weight2, weight3, weight4, hx_, cx_tmp, output, hy_, cy_, grad_output, grad_hy, grad_cy, reverse, mode, hidden_size, num_layers, has_biases, train, bidirectional, batch_sizes, batch_first, workspace, out0, out1, out2, out3, out4, out5, out6);
}
// aten::mkldnn_rnn_layer_backward.out(Tensor input, Tensor weight1, Tensor weight2, Tensor weight3, Tensor weight4, Tensor hx_, Tensor cx_tmp, Tensor output, Tensor hy_, Tensor cy_, Tensor? grad_output, Tensor? grad_hy, Tensor? grad_cy, bool reverse, int mode, int hidden_size, int num_layers, bool has_biases, bool train, bool bidirectional, int[] batch_sizes, bool batch_first, Tensor workspace, *, Tensor(a!) out0, Tensor(b!) out1, Tensor(c!) out2, Tensor(d!) out3, Tensor(e!) out4, Tensor(f!) out5, Tensor(g!) out6) -> (Tensor(a!), Tensor(b!), Tensor(c!), Tensor(d!), Tensor(e!), Tensor(f!), Tensor(g!))
inline ::std::tuple<at::Tensor &,at::Tensor &,at::Tensor &,at::Tensor &,at::Tensor &,at::Tensor &,at::Tensor &> mkldnn_rnn_layer_backward_outf(const at::Tensor & input, const at::Tensor & weight1, const at::Tensor & weight2, const at::Tensor & weight3, const at::Tensor & weight4, const at::Tensor & hx_, const at::Tensor & cx_tmp, const at::Tensor & output, const at::Tensor & hy_, const at::Tensor & cy_, const ::std::optional<at::Tensor> & grad_output, const ::std::optional<at::Tensor> & grad_hy, const ::std::optional<at::Tensor> & grad_cy, bool reverse, int64_t mode, int64_t hidden_size, int64_t num_layers, bool has_biases, bool train, bool bidirectional, at::IntArrayRef batch_sizes, bool batch_first, const at::Tensor & workspace, at::Tensor & out0, at::Tensor & out1, at::Tensor & out2, at::Tensor & out3, at::Tensor & out4, at::Tensor & out5, at::Tensor & out6) {
    return at::_ops::mkldnn_rnn_layer_backward_out::call(input, weight1, weight2, weight3, weight4, hx_, cx_tmp, output, hy_, cy_, grad_output, grad_hy, grad_cy, reverse, mode, hidden_size, num_layers, has_biases, train, bidirectional, batch_sizes, batch_first, workspace, out0, out1, out2, out3, out4, out5, out6);
}

}
