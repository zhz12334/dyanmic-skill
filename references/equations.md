# Core Equations Reference

## Linear MDOF dynamics
M q_ddot + C q_dot + K q = f(t)

## Undamped modal problem
K phi_i = omega_i^2 M phi_i

## Natural frequency
f_i = omega_i / (2*pi)

## Modal damping ratio for Rayleigh damping
zeta_i = alpha/(2*omega_i) + beta*omega_i/2

## Frequency response
H(omega) = (-omega^2 M + i*omega*C + K)^(-1)

## Modal Assurance Criterion
MAC(phi_a, phi_b) = |phi_a^H phi_b|^2 / ((phi_a^H phi_a)(phi_b^H phi_b))

## Frequency relative error
error_i = |f_ref_i - f_model_i| / f_ref_i

## PSD-to-RMS
x_rms = sqrt(integral S_xx(f) df)

Always verify one-sided/two-sided PSD conventions before numerical integration.
