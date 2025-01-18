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
#include <ATen/ops/max_meta.h>

namespace at {
namespace native {
struct TORCH_API structured_max_out : public at::meta::structured_max_dim {
void impl(const at::Tensor & self, int64_t dim, bool keepdim, const at::Tensor & max, const at::Tensor & max_values);
};
struct TORCH_API structured_max_out_mps : public at::meta::structured_max_dim {
void impl(const at::Tensor & self, int64_t dim, bool keepdim, const at::Tensor & max, const at::Tensor & max_values);
};
TORCH_API ::std::tuple<at::Tensor,at::Tensor> qmax(const at::Tensor & self, int64_t dim, bool keepdim=false);
TORCH_API ::std::tuple<at::Tensor,at::Tensor> max(const at::Tensor & self, at::Dimname dim, bool keepdim=false);
TORCH_API ::std::tuple<at::Tensor &,at::Tensor &> max_out(const at::Tensor & self, at::Dimname dim, bool keepdim, at::Tensor & max, at::Tensor & max_values);
TORCH_API at::Tensor max(const at::Tensor & self);
TORCH_API at::Tensor & max_unary_out(const at::Tensor & self, at::Tensor & out);
TORCH_API at::Tensor max_mps(const at::Tensor & self);
TORCH_API at::Tensor max_quantized_cpu(const at::Tensor & self);
TORCH_API at::Tensor & max_quantized_unary_out(const at::Tensor & self, at::Tensor & out);
TORCH_API at::Tensor max(const at::Tensor & self, const at::Tensor & other);
TORCH_API at::Tensor & max_out(const at::Tensor & self, const at::Tensor & other, at::Tensor & out);
} // namespace native
} // namespace at
