import React from "react";
import { Button, Modal, ModalHeader,
    ModalContent,
    ModalActions} from "semantic-ui-react";
import { useState } from 'react';

const OperationsPanel = ({ onOperation, documentVersion }) => {
    const [showAddColumnModalOpen, setShowAddColumnModalOpen] = useState(false);
    const [showFilterRowModal, setShowFilterRowModal] = useState(false);
    const [showCombineColumnModal, setShowCombineColumnModal] = useState(false);

    return (
        <div className="operations-panel">
            <div className="operations-grid">
                <Button onClick={() => setShowAddColumnModalOpen(true)}>Add Column (Sum)</Button>
                <Button onClick={() => setShowFilterRowModal(true)}>Filter</Button>
                <Button onClick={() => setShowCombineColumnModal(true)}>Combine Columns</Button>
                <Button onClick={() => onOperation("undo", {})} disabled={documentVersion < 2}>Undo</Button>
            </div>
            { showAddColumnModalOpen ? <AddColumnModal 
                open={showAddColumnModalOpen}
                onClose={() => setShowAddColumnModalOpen(false)}
                onAddColumn={onOperation}
            />: null}
            { showFilterRowModal ? <FilterRowsModal
                open={showFilterRowModal}
                onClose={() => setShowFilterRowModal(false)}
                onFilter={onOperation}
            />: null}
            {showCombineColumnModal ? <CombineColumnsModal
                open={showCombineColumnModal}
                onClose={() => setShowCombineColumnModal(false)}
                onCombineColumns={onOperation}
            />: null}
            </div>
    );
};

const AddColumnModal = ({ open, onClose, onAddColumn }) => {
    const [columnName1, setColumnName1] = useState("");
    const [columnName2, setColumnName2] = useState("");
    const [newColumnName, setNewColumnName] = useState("");

    const handleAddColumn = () => {
        onAddColumn("addColumn", { columnName1, columnName2, newColumnName });
        onClose();
    };

    return (
        <Modal open={open} onClose={onClose} closeIcon>
            <ModalHeader>Sum of Column</ModalHeader>
            <ModalContent>
                <div>
                    <label>Column 1:</label>
                    <input
                        type="text"
                        value={columnName1}
                        onChange={(e) => setColumnName1(e.target.value)}
                    />
                    <label>+ Column 2:</label>
                    <input
                        type="text"
                        value={columnName2}
                        onChange={(e) => setColumnName2(e.target.value)}
                    />
                    <label>New Column Name:</label>
                    <input
                        type="text"
                        value={newColumnName}
                        onChange={(e) => setNewColumnName(e.target.value)}
                    />
                </div>
            </ModalContent>
            <ModalActions>
                <Button onClick={onClose}>Cancel</Button>
                <Button onClick={handleAddColumn} primary>
                    Add Column
                </Button>
            </ModalActions>
        </Modal>
    );
};

const FilterRowsModal = ({ open, onClose, onFilter}) => {
    const [condition, setCondition] = useState("");

    const handleFilterRows = () => {
        onFilter("filterRows", { condition });
        onClose();
    };

    return (
        <Modal open={open} onClose={onClose} closeIcon>
            <ModalHeader>Filter Rows</ModalHeader>
            <ModalContent>
                <div>Condition Ecample: Price > 100</div>
                <div>
                    <label>Condition:</label>
                    <input
                        type="text"
                        value={condition}
                        onChange={(e) => setCondition(e.target.value)}
                    />
                </div>
            </ModalContent>
            <ModalActions>
                <Button onClick={onClose}>Cancel</Button>
                <Button onClick={handleFilterRows} primary>
                    Filter Rows
                </Button>
            </ModalActions>
        </Modal>
    );
}

const CombineColumnsModal = ({ open, onClose, onCombineColumns }) => {
    const [columnName1, setColumnName1] = useState("");
    const [columnName2, setColumnName2] = useState("");
    const [separator, setSeparator] = useState("");
    const [newColumnName, setNewColumnName] = useState("");

    const handleCombineColumns = () => {
        onCombineColumns("combineColumns", { columnName1, columnName2, separator, newColumnName });
        onClose();
    };

    return (
        <Modal open={open} onClose={onClose} closeIcon>
            <ModalHeader>Combine Columns</ModalHeader>
            <ModalContent style={{display: "flex"}}>
                <div>
                    <label>Column 1:</label>
                    <input
                        type="text"
                        value={columnName1}
                        onChange={(e) => setColumnName1(e.target.value)}
                    />
                </div>
                <div>
                    <label>Column 2:</label>
                    <input
                        type="text"
                        value={columnName2}
                        onChange={(e) => setColumnName2(e.target.value)}
                    />
                </div>
                <div>
                    <label>Separator:</label>
                    <input
                        type="text"
                        value={separator}
                        onChange={(e) => setSeparator(e.target.value)}
                    />
                </div>
                <div>
                    <label>New Column Name:</label>
                    <input
                        type="text"
                        value={newColumnName}
                        onChange={(e) => setNewColumnName(e.target.value)}
                    />
                </div>
            </ModalContent>
            <ModalActions>
                <Button onClick={onClose}>Cancel</Button>
                <Button onClick={handleCombineColumns} primary>
                    Combine Columns
                </Button>
            </ModalActions>
        </Modal>
    );
};

export default OperationsPanel;