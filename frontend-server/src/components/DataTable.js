import React from "react";
import { Table, Loader } from "semantic-ui-react";

const DataTable = ({ data, showLoader }) => {
    const {
        data: rowData = [],
        columns = []
    } = data;
    if (showLoader) return <Loader content='Loading' inline='centered'/>;
    if (rowData.length === 0) return <p>No data available</p>;

    return (
        <div className="data-table">
            <Table celled>
                <Table.Header>
                    <Table.Row>
                        {columns.map((key) => (
                            <Table.HeaderCell key={key}>{key}</Table.HeaderCell>
                        ))}
                    </Table.Row>
                </Table.Header>
                <Table.Body>
                    {rowData.map((row, index) => (
                        <Table.Row key={index}>
                            {columns.map((value, i) => (
                                <Table.Cell key={i}>{row[value]}</Table.Cell>
                            ))}
                        </Table.Row>
                    ))}
                </Table.Body>
            </Table>
        </div>
    );
};

export default DataTable;