// components/dashboard/DashboardClient.tsx
'use client';

import { Card, Row, Col, Spinner } from 'react-bootstrap';

export default function DashboardClient() {
  return (
    <div>
      <h1 className="mb-4">ダッシュボード</h1>
      
      <Row className="mb-4">
        <Col md={3}>
          <Card className="border-primary mb-3 h-100">
            <Card.Body>
              <div className="d-flex justify-content-between">
                <div>
                  <Card.Title className="text-muted">車両総数</Card.Title>
                  <Card.Text className="fs-2 fw-bold">24</Card.Text>
                </div>
                <div className="fs-1 text-muted">🚚</div>
              </div>
            </Card.Body>
          </Card>
        </Col>
        {/* 他の統計カード */}
      </Row>
      
      {/* 他のセクション */}
    </div>
  );
}