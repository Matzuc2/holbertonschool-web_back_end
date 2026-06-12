-- create an index on firt letter for score and name
CREATE INDEX idx_name_first_score
ON names(name(1),score)