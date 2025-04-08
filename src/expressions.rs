use polars::prelude::*;
use pyo3_polars::derive::polars_expr;
use std::fmt::Write;
use rust_stemmers::{Algorithm, Stemmer};

#[polars_expr(output_type=String)]
fn snowball_stem(inputs: &[Series]) -> PolarsResult<Series> {
    let ca: &StringChunked = inputs[0].str()?;
    let en_stemmer = Stemmer::create(Algorithm::English);
    let out: StringChunked = ca.apply_into_string_amortized(|value: &str, output: &mut String| {
        write!(output, "{}", en_stemmer.stem(value)).unwrap()
    });
    Ok(out.into_series())
}