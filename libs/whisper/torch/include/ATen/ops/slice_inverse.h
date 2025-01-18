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



#include <ATen/ops/slice_inverse_ops.h>

namespace at {


// aten::slice_inverse(Tensor(a) self, Tensor src, int dim=0, SymInt? start=None, SymInt? end=None, SymInt step=1) -> Tensor(a)
inline at::Tensor slice_inverse(const at::Tensor & self, const at::Tensor & src, int64_t dim=0, ::std::optional<int64_t> start=::std::nullopt, ::std::optional<int64_t> end=::std::nullopt, int64_t step=1) {
    return at::_ops::slice_inverse::call(self, src, dim, start.has_value() ? ::std::make_optional(c10::SymInt(*start)) : ::std::nullopt, end.has_value() ? ::std::make_optional(c10::SymInt(*end)) : ::std::nullopt, step);
}
namespace symint {
  template <typename T, typename = std::enable_if_t<std::is_same<T, int64_t>::value>>
  at::Tensor slice_inverse(const at::Tensor & self, const at::Tensor & src, int64_t dim=0, ::std::optional<int64_t> start=::std::nullopt, ::std::optional<int64_t> end=::std::nullopt, int64_t step=1) {
    return at::_ops::slice_inverse::call(self, src, dim, start.has_value() ? ::std::make_optional(c10::SymInt(*start)) : ::std::nullopt, end.has_value() ? ::std::make_optional(c10::SymInt(*end)) : ::std::nullopt, step);
  }
}

// aten::slice_inverse(Tensor(a) self, Tensor src, int dim=0, SymInt? start=None, SymInt? end=None, SymInt step=1) -> Tensor(a)
inline at::Tensor slice_inverse_symint(const at::Tensor & self, const at::Tensor & src, int64_t dim=0, ::std::optional<c10::SymInt> start=::std::nullopt, ::std::optional<c10::SymInt> end=::std::nullopt, c10::SymInt step=1) {
    return at::_ops::slice_inverse::call(self, src, dim, start, end, step);
}
namespace symint {
  template <typename T, typename = std::enable_if_t<std::is_same<T, c10::SymInt>::value>>
  at::Tensor slice_inverse(const at::Tensor & self, const at::Tensor & src, int64_t dim=0, ::std::optional<c10::SymInt> start=::std::nullopt, ::std::optional<c10::SymInt> end=::std::nullopt, c10::SymInt step=1) {
    return at::_ops::slice_inverse::call(self, src, dim, start, end, step);
  }
}

}
