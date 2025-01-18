#pragma once

// @generated by torchgen/gen.py from NativeFunction.h

#include <c10/core/Scalar.h>
#include <c10/core/Storage.h>
#include <c10/core/TensorOptions.h>
#include <c10/util/Deprecated.h>
#include <optional>
#include <c10/core/QScheme.h>
#include <ATen/core/Reduction.h>
#include <ATen/core/Tensor.h>
#include <tuple>
#include <vector>


namespace at {
namespace native {
TORCH_API ::std::tuple<::std::vector<at::Tensor>,::std::vector<at::Tensor>,::std::vector<at::Tensor>,::std::vector<at::Tensor>> _fused_adagrad(at::TensorList self, at::TensorList grads, at::TensorList state_sums, at::TensorList state_steps, double lr, double lr_decay, double weight_decay, double eps, bool maximize, const ::std::optional<at::Tensor> & grad_scale={}, const ::std::optional<at::Tensor> & found_inf={});
TORCH_API void _fused_adagrad_out(at::TensorList self, at::TensorList grads, at::TensorList state_sums, at::TensorList state_steps, double lr, double lr_decay, double weight_decay, double eps, bool maximize, const ::std::optional<at::Tensor> & grad_scale, const ::std::optional<at::Tensor> & found_inf, at::TensorList out);
TORCH_API void _fused_adagrad_kernel_cpu_(at::TensorList self, at::TensorList grads, at::TensorList state_sums, at::TensorList state_steps, double lr, double lr_decay, double weight_decay, double eps, bool maximize, const ::std::optional<at::Tensor> & grad_scale={}, const ::std::optional<at::Tensor> & found_inf={});
} // namespace native
} // namespace at
