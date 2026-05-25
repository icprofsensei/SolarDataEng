import polars as pl

def repd_proc(df):
    for c in ['Record Last Updated (dd/mm/yyyy)','Under Construction', 'Operational', 'Planning Application Submitted', 'Planning Permission Refused', 'Planning Application Withdrawn',
              'Appeal Lodged', 'Appeal Withdrawn', 'Appeal Refused', 'Planning Permission Expired', 'Planning Permission  Granted', 'Secretary of State - Intervened', 
              'Secretary of State - Refusal', 'Secretary of State - Granted']:
        df = df.with_columns(
            # Date objects have to be formatted with a minimum of 8 digits
            pl.when(pl.col(c).str.len_chars() < 8).then(None).otherwise(pl.col(c)).name.keep().str.to_date()
        )
    return df

