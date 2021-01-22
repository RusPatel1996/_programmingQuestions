function get_prefix_value(matrix, prefix_matrix, prefix_row, row, col) {

    // first row and column element
    if (row == 0 && col == 0) return matrix[0][0];

    let index_value = matrix[row][col];

    // first row
    let left_value = prefix_row[col - 1];
    if (row == 0) return left_value + index_value;

    // first column
    let top_value = prefix_matrix[row - 1][col];
    if (col == 0) return top_value + index_value;

    // rest of the values
    let left_diag_value = prefix_matrix[row - 1][col - 1];
    return top_value + left_value + index_value - left_diag_value;
}

function get_prefix_matrix(matrix) {
    let prefix_matrix = [];
    let row_length = matrix.length;
    let col_length = matrix[0].length;

    for (row = 0; row < row_length; row++) {
        let prefix_row = [];

        for (col = 0; col < col_length; col++) {
            prefix_row.push(get_prefix_value(matrix, prefix_matrix, prefix_row, row, col));
        }
        prefix_matrix.push(prefix_row);
    }

    return prefix_matrix;
}

function get_sum(matrix, row_1, col_1, row_2, col_2) {
    let prefix_matrix = get_prefix_matrix(matrix);

    console.log(prefix_matrix);

    let total_sum = prefix_matrix[row_2][col_2];
    if (row_1 == 0 && col_1 == 0) return total_sum;
    //if (row_1 == row_2 && col_1 == col_2) return matrix[row_1][col_1];

    let overlapping_left_section_sum = 0;
    let overlapping_top_section_sum = 0;

    if (row_1 == 0) {
        overlapping_left_section_sum = prefix_matrix[row_2][col_1 - 1];
        return total_sum - overlapping_left_section_sum;
    }

    if (col_1 == 0) {
        overlapping_top_section_sum = prefix_matrix[row_1 - 1][col_2];
        return total_sum - overlapping_top_section_sum;
    }

    overlapping_left_section_sum = prefix_matrix[row_2][col_1 - 1];
    overlapping_top_section_sum = prefix_matrix[row_1 - 1][col_2];
    let overlapping_left_diag_section_sum = prefix_matrix[row_1 - 1][col_1 - 1];
    return total_sum - overlapping_left_section_sum - overlapping_top_section_sum + overlapping_left_diag_section_sum;
}

function main() {
    let matrix = [
        [7, 7, 0],
        [-4, -7, 7],
        [-4, 0, -2],
        [-8, -5, 6]
    ];

    if (matrix == null) {
        return;
    }

    row_1 = 3;
    col_1 = 2;
    row_2 = 3;
    col_2 = 2;
    let sum_query = get_sum(matrix, row_1, col_1, row_2, col_2);

    console.log(sum_query); // --> 9
}

main()