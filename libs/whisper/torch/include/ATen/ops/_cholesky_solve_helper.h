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



#include <ATen/ops/_cholesky_solve_helper_ops.h>

namespace at {


// aten::_cholesky_solve_helper(Tensor self, Tensor A, bool upper) -> Tensor
inline at::Tensor _cholesky_solve_helper(const at::Tensor & self, const at::Tensor & A, bool upper) {
    return at::_ops::_cholesky_solve_helper::call(self, A, upper);
}

// aten::_cholesky_solve_helper.out(Tensor self, Tensor A, bool upper, *, Tensor(a!) out) -> Tensor(a!)
inline at::Tensor & _cholesky_solve_helper_out(at::Tensor & out, const at::Tensor & self, const at::Tensor & A, bool upper) {
    return at::_ops::_cholesky_solve_helper_out::call(self, A, upper, out);
}
// aten::_cholesky_solve_helper.out(Tensor self, Tensor A, bool upper, *, Tensor(a!) out) -> Tensor(a!)
inline at::Tensor & _cholesky_solve_helper_outf(const at::Tensor & self, const at::Tensor & A, bool upper, at::Tensor & out) {
    return at::_ops::_cholesky_solve_helper_out::call(self, A, upper, out);
}

}
