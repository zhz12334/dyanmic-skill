# Clean-Room Reproduction Gate

The final package must be exercised in a fresh environment that does not inherit developer caches, undeclared files or interactive state.

## Procedure
1. start from frozen package only;
2. verify artifact hashes;
3. follow README exactly;
4. install declared dependencies;
5. obtain permitted data using documented steps;
6. run smoke/tests;
7. run reproduction entrypoint;
8. regenerate metrics/figures;
9. compare against acceptance bounds;
10. record every manual intervention.

## Failure examples
- hidden absolute path
- undeclared local data
- missing dependency
- cached trained model
- manual GUI step absent from README
- environment variable not documented
- nondeterministic result outside stated uncertainty
